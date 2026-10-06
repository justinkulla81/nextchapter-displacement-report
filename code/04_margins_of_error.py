#!/usr/bin/env python3
"""90% margins of error for January-August comparisons using the BLS generalized variance
function (GVF) method and published CPS parameters/factors (data/bls_gvf_parameters.json).
Eight-month average factors are interpolated linearly between BLS 3- and 12-month factors;
year-apart changes apply the ratio of the published change-in-yearly-average factor to the
yearly-average factor. Comparisons with 2019 treat periods as independent.
Run: python3 04_margins_of_error.py"""
import json,math
P=json.load(open('../data/bls_gvf_parameters.json'))['rows']; D=json.load(open('../data/cps_aggregates_jan_aug_2019_2025_2026.json'))
Z=1.645
def favg(r,m=8): return r['f_q']+(m-3)/9*(r['f_y']-r['f_q'])
def fchg(r,m=8): return favg(r,m)*r['f_cy']/r['f_y']
def se_level(r,x,N): return math.sqrt(max((r['a']+r['b']*N)*(x-x*x/N),0))
def se_pct(r,p,y): v=((r['a']+r['b']*y)/y)*p*(100-p); return math.sqrt(v) if v>0 else float('nan')
K=1000.0
def g(y,k): return D[y]['G'][k]
def N(y): return D[y]['P']['pop16'][0]*K
UROW={'occ_1':'unemployed_mgmt_bus_fin','occ_2':'unemployed_mgmt_bus_fin','wc':'unemployed_mgmt_prof','occ_17':'unemployed_office_admin'}
def urow(k):
    if k in UROW: return P[UROW[k]]
    if k.startswith('occ_') and int(k[4:]) in range(3,11): return P['unemployed_professional']
    if k.startswith('wc'): return P['unemployed_mgmt_prof']
    return P['unemployed_total']
def share(k,y): G=g(y,k); return 100*G[2]/G[1], G[1]*K
def ltu_share_change(k,y1='2026',y0='2025'):
    p1,u1=share(k,y1);p0,u0=share(k,y0); r=P['pct_27wk_of_unemployed']
    if y0=='2019':
        se=math.sqrt((favg(r)*se_pct(r,p1,u1))**2+(favg(r)*se_pct(r,p0,u0))**2)
    else:
        se=fchg(r)*se_pct(r,(p1+p0)/2,(u1+u0)/2)
    return p1,p0,p1-p0,Z*se
def rate_change(k,idx,y1='2026',y0='2025',row=None):
    # idx 1 = unemployed, 2 = LTU ; rate = level/LF
    r=row or (P['unemployed_27wk_level'] if idx==2 else urow(k))
    G1,G0=g(y1,k),g(y0,k); x1,x0=G1[idx]*K,G0[idx]*K; L1,L0=G1[0]*K,G0[0]*K
    r1,r0=100*x1/L1,100*x0/L0
    if y0=='2019':
        se=math.sqrt((favg(r)*se_level(r,x1,N(y1))/L1)**2+(favg(r)*se_level(r,x0,N(y0))/L0)**2)*100
    else:
        se=fchg(r)*se_level(r,(x1+x0)/2,(N(y1)+N(y0))/2)/((L1+L0)/2)*100
    return r1,r0,r1-r0,Z*se
def part_change(k,y1='2026',y0='2025'):
    r=P['labor_force_level']; a1,a0=D[y1]['P'][k],D[y0]['P'][k]
    p1,p0=100*a1[1]/a1[0],100*a0[1]/a0[0]
    if y0=='2019': se=math.sqrt((favg(r)*se_level(r,a1[1]*K,N(y1))/(a1[0]*K))**2+(favg(r)*se_level(r,a0[1]*K,N(y0))/(a0[0]*K))**2)*100
    else: se=fchg(r)*se_level(r,(a1[1]+a0[1])/2*K,(N(y1)+N(y0))/2)/((a1[0]+a0[0])/2*K)*100
    return p1,p0,p1-p0,Z*se
def fmt(t): return f"{t[0]:.2f} vs {t[1]:.2f}: {t[2]:+.2f} ±{t[3]:.2f} {'BEYOND' if abs(t[2])>t[3] else 'within'}"
rows=[]
def out(lbl,t,old=''): rows.append((lbl,t,old)); print(f"{lbl:42} {fmt(t):40} old {old}")
out('WC LTU rate (% of WC LF)',rate_change('wc',2),'±0.11')
out('WC unemployment rate',rate_change('wc',1),'±0.21')
out('WC LTU share',ltu_share_change('wc'),'±3.6')
out('All LTU share',ltu_share_change('all'),'±1.8')
for k,lbl,old in [('occ_3','Computer & math','±11.6'),('occ_2','Business & fin','±9.7'),('occ_1','Management','±7.3'),('occ_4','Arch & eng','±20.5'),('occ_17','Office admin','±6.3'),('occ_9','Arts design','±11.2'),('occ_10','Health pract','±11.5'),('occ_8','Education','±7.2')]:
    out('LTU share '+lbl,ltu_share_change(k),old)
for k,lbl,old in [('wc_ind_7','Information','±17.2'),('wc_ind_9','Prof & bus svc','±8.1'),('wc_ind_8','Financial','±14.4'),('wc_ind_4','Manufacturing','±14.5'),('wc_ind_13','Public admin','±17.1'),('wc_ind_10','Educ & health','±5.7')]:
    out('WC LTU share ind '+lbl,ltu_share_change(k),old)
for k,lbl,old in [('wc_age_u35','<35','±5.7'),('wc_age_35_44','35-44','±7.9'),('wc_age_45_54','45-54','±8.6'),('wc_age_55_64','55-64','±9.2'),('wc_age_65p','65+','±12.5')]:
    out('WC LTU share age '+lbl,ltu_share_change(k),old)
out('WC 50+ LTU share',ltu_share_change('wc_50p'),'±6.5')
out('Participation 55+',part_change('pop55'),'±0.5')
out('Participation 55+ vs 2019',part_change('pop55','2026','2019'),'')
out('Unemp rate 25-34',rate_change('age_25_34',1),'sig')
out('Grad BA 22-27 unemp vs 2019',rate_change('grad_ba',1,'2026','2019'),'±0.9')
out('Grad BA 22-27 unemp vs 2025',rate_change('grad_ba',1),'')
out('WC LTU rate vs 2019',rate_change('wc',2,'2026','2019'),'')
# wc vs blue share (independent groups, same year)
r=P['pct_27wk_of_unemployed']; p1,u1=share('wc','2026'); p2,u2=share('blue','2026')
se=math.sqrt((favg(r)*se_pct(r,p1,u1))**2+(favg(r)*se_pct(r,p2,u2))**2)
out('WC vs blue LTU share 2026',(p1,p2,p1-p2,Z*se),'sig')
# job losers
for y in ['2026','2025']:
    G=g(y,'wc'); print(y,'WC job-loser LTU rate', round(100*G[5]/G[0],3), 'share of WC LTU that are job losers', round(100*G[5]/G[2],1))
r_jl=rate_change('wc',5,row=P['unemployed_27wk_level'])
out('WC job-loser LTU rate',r_jl,'')
r_jl19=rate_change('wc',5,'2026','2019',row=P['unemployed_27wk_level'])
out('WC job-loser LTU rate vs 2019',r_jl19,'')
json.dump([(l,list(t),o) for l,t,o in rows],open('../data/margins_of_error_results.json','w'),indent=0)
print('--- unemployment rates')
for k in ['occ_3','occ_2','occ_1','occ_4','occ_17','occ_9','occ_10','occ_8','all','wc_ind_7','wc_ind_9','wc_ind_8','wc_ind_4','wc_ind_13','wc_ind_10','wc_age_u35','wc_age_35_44','wc_age_45_54','wc_age_55_64','wc_age_65p','age_55_64','age_65p']:
    print(k, fmt(rate_change(k,1)))
print('blue unemp',fmt(rate_change('blue',1)),'blue share',fmt(ltu_share_change('blue')))
print('hs2227 vs2019',fmt(rate_change('hs2227',1,'2026','2019')),'hs vs 2025',fmt(rate_change('hs2227',1)))
print('grad share ltu',fmt(ltu_share_change('grad_ba')),'hs share',fmt(ltu_share_change('hs2227')))
print('wc50 vs 2019',fmt(ltu_share_change('wc_50p','2026','2019')))
print('part65',fmt(part_change('pop65')))
