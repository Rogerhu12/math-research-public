"""Archive the logical gluing corollary; verify identities, not a new PDE solve."""
from pathlib import Path
import json,gzip,hashlib
B=Path('/workspace/scratch/d1aa462cfc02');T=B/'math-research/topics/visible-flex-larger-amplitude'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):
    raw=p.read_bytes();return json.loads(gzip.decompress(raw) if p.suffix=='.gz' else raw)
def fresh(p,s):
    if p.exists():assert p.read_text()==s,str(p)
    else:p.write_text(s)
pins={
'R141':('notes/2026-11-13-root-restricted-outer-r6-cont-r1-certificate.json.gz','b9acf8f7492f9f85f9cf010868d61348082b8cd4e1e11d12d5b195f9f97f3582'),
'R143':('notes/2026-11-13-root-full-cut-homothetic-contraction-r1.json','e76e2e452079afec5d05939a8f8ddd79ed7bf1e656446ac5576086efebd47e83'),
'R142':('notes/2026-11-13-exact-resume-r127-mean-height-bridge-r1.json','b26c36452bc651f8d1ce55f9da23b6c904ad209878c268787a38cdce45612ae5')}
docs={};inputs={}
for key,(name,want) in pins.items():
    p=T/name;assert sha(p)==want;docs[key]=read(p);assert docs[key]['all_gates'] and all(docs[key]['gates'].values());inputs[key]={'path':name,'sha256':want}
f,c,h=docs['R141'],docs['R143'],docs['R142']
assert f['original_two_cell_low46_parameter_selfmap_certified'] and f['same_existing_R127_field']
assert c['unique_real_fixed_point_in_K_and_original_working_domain'] and c['inputs']['full_field']['sha256']==pins['R141'][1]
assert h['original_R127_full_frequency_fixed_point_consumed'] and h['inner_tail_gluing_requires_same_full_parameter_cut']
assert h['inputs']['joint_certificate']['sha256']=='36242d95a210e6aee3e38c994d0a70b61fa1fbb2df672a9ab3f4783bcca93ca1'
assert h['complete_mean_equation_restored_by_positive_weight_identity'] and h['complete_Darboux_height_on_original_two_cells'] and h['single_global_height_integration_constant']
assert f['complete_mean_inverse_and_infinite_high_retained'] and h['complete_mean_and_inverse_retained']
proofs=['results/R100-hybrid46-parameter-chart-and-source-transfer.md','results/R127-complete-low-middle-high-mixed-boundary-family.md','results/R141-complete-two-cell-low46-cut-existence.md','results/R142-full-mean-height-and-nested-annulus-bridge.md','results/R143-full-cut-homothetic-Cauchy-contraction.md']
inputs['proofs']=[{'path':name,'sha256':sha(T/name)} for name in proofs]
proof=r'''# R145：完整切口解除node12条件，原内尾与两外胞元精确C²接合

作者：/root（GPT-6 Astra Pro，AI辅助），2026-11-13。状态：已证明的接合推论；没有新增数值求解。R142第6节原先以完整切口方程为条件，此条件现在由R141存在及R143唯一性支付。

## 1. 同一参数、同一度量和同一无穷尾

取R143工作体K中唯一实参数\(a_*\)。K的S半径3/8、T共同半径1/64及40轴2b包含于R100原全频内头域，也包含于R127原S单位/T半径1/32外场域。令I为R100在\(a_*\)的真实内场，O为R127在同一\(a_*\)的真实外场。I保原全部213胞元、完整mean、全部低/中/无限高以及独立far未知量，并接R18原无穷C²尾；O保原cells11/10和完整方程。

所有背景使用原R26实际度量

\[
g=(1+w(r)^2)\,dr^2+r^2d\theta^2.
\]

节点12的真实半径、w和w_r为同一物理对象。本文不借新q122的数值g，不换轴，也不把已有中高帽解释成有限支持。

## 2. 低频高度一致后，完整非均值动量也一致

R100使用原canonical浅高度Q，物理高度为\(H_m(b)=b^4Q_m(b)\)。R141真实固定点方程精确匹配全部46低模式的Q，因此物理非均值高度也匹配；\(b>0\)，没有额外w或Fourier pair 2。

低频Green的内端是原混合边界。用其原canonical动量记号写为

\[
\Xi_O-B_0Q_O=\beta(a_*),\qquad
\beta(a_*)=\Xi_I-B_0Q_I.
\]

这里\(\beta\)是完整真实非线性DN减同高度的线性DN，保全部mean/inverse/far。由\(Q_O=Q_I\)立即得\(\Xi_O=\Xi_I\)。不能在高度尚未匹配时把这个Robin条件读成独立的动量Dirichlet条件。

原端口变换在同一正r,w上可逆，故全部低频物理\(P=h_\theta/(rw)\)、\(\bar K=h_{\perp,r}/w\)一致。m≥94的全部偶频物理P和K在R127中本来就按同一真实内头的完整初始迹指定，所以这些频率也一致。两边在共同正角宽解析，因此这些恒等式的所有所需角导数也相同。这没有用有限46模式替代其余无穷频率。

## 3. 一个完整均值根和一个高度常数

同一节点上的P、\(\bar K\)及角导数给同一完整holonomy均值方程。两边都是已支付正分支的小根；R142实际正隐式导数界给该分支唯一性，所以完整零模c也一致，\(K=c+\bar K\)不是新增自由参数。

保留内尾原有的cuff高度规范，只将外侧一个积分常数选为I在node12的均值高度。外侧沿整个11/10区间使用同一积分

\[
h_{O,0}(r)=h_{I,0}(b)+\int_b^r w(\rho)(1+c(\rho))\,d\rho .
\]

这不重置node11高度，不额外施加末端mean slope或第二个mean height条件。全高度及一阶导数因此匹配：

\[
h_O=h_I,\qquad h_{O,\theta}=h_{I,\theta},
\qquad h_{O,r}=h_{I,r}.
\]

纯角二阶及混合二阶导数由相同解析迹得到。剩余径向二阶导数由两边同一完整Darboux方程确定。用R142原符号

\[
T=P_\theta,\quad U=\bar K_\theta-P,\quad
E=1+w^2,\quad L=1+K+ET>0
\]

可写

\[
h_{rr}-w_r=
\frac{EwU^2/r+w_r(-K-T+w^2KT-w^2P^2)}{L}.
\]

分母正门已付；右侧全部变量及背景在节点相同，故\(h_{O,rr}=h_{I,rr}\)。完整物理二jet严格相等，而非仅落在相交的数值区间。这给原内侧12..224及无穷尾与外侧11/10之间的单一C² Darboux高度。

## 4. 平面发展和三维接合只用一次刚体规范

在节点邻域，\(q=g-dh^2\)为同一正定平坦metric。R142/R41的完整连接给

\[
X_\theta=a\,t,\qquad X_r=u\,t+v\,n,\qquad
\gamma_\theta=\Omega,\qquad\gamma_r=\Gamma(P,K,P_\theta,K_\theta).
\]

两边的a,u,v,Ω及Γ由同一物理迹决定。先用一次平面旋转匹配一个角点的γ，再用一次平面平移匹配该点X；相同角向方程便使整条node12曲线和完整切向框架一致。两边径向方程及完整PDE随后给相同一、二阶物理导数。故\(F=(X,h)\)在node12作同一g的C²等距接合。

其周期性由已付完整mean和偶频半周恒等式保持，未另加角向平移holonomy条件。I的独立far坐标和原无穷C²平坦cuff极限完全保留：本文只在其外面接O，没有更改任何内侧解或重设深端数据。

参数在R143原工作域内唯一；固定内尾的cuff规范后，两边场在各自既有认证球中唯一，剩余整体刚体规范只统一选取一次。这里不声称全参数空间唯一，也不凭接合推出整个内侧或未来外侧的全局无自交。

## 5. 精确完成范围与下一真实端口

已付的是原内尾与原外11/10之间的全部频率、完整mean、单一高度和C² seam。R142的两胞元嵌入环带结论仍有效；更大整个拼接区域的全局embedding、reach和可见运动并未从局部接合自动推出。

当前真实外端就是node10的完整Cauchy迹。其严格正无限尾、真实mean和累计高度都须继续进入原9..0；没有免费角宽提升，也没有以有限候选径向导数替换真方程。固定握持区、全闭面、全t同g和README幅度/精化门仍未完成。

本条仅作逻辑推论和实际输入身份消费。R141主b9acf8f7…、R143主e76e2e45…、R142主b26c3645…均原字节，R142所指R127仍为36242d95…；完整SHA与所有所用证明身份列在gluing-input-identity.json。本条没有新增ODE、积分、Newton或声称新的数值误差门。
'''
pp=T/'results/R145-exact-inner-tail-two-cell-C2-gluing.md';fresh(pp,proof)
ledger=T/'notes/2026-11-13-root-inner-tail-two-cell-gluing-input-identity.json'
fresh(ledger,json.dumps({'schema':'logical-C2-gluing-input-identity-v1','inputs':inputs,'same_complete_R127_field_verified':True,'same_original_R100_inner_field_used':True,'conditional_R142_full_cut_hypothesis_discharged_by_R141_R143':True,'no_new_numerical_certificate_claimed':True},indent=2)+'\n')
src=T/'computations/root_archive_inner_tail_two_cell_gluing.py';fresh(src,Path(__file__).read_text())
records=[{'path':str(p.relative_to(T)),'sha256':sha(p),'bytes':p.stat().st_size} for p in [pp,ledger,src]]
manifest=T/'notes/2026-11-13-root-inner-tail-two-cell-gluing-manifest.json';fresh(manifest,json.dumps({'schema':'exact-inner-tail-two-cell-C2-gluing-proof-archive-v1','files':records},indent=2)+'\n')
spec=[{'id':'r145-exact-inner-tail-C2-gluing','manifest':str(manifest.relative_to(T)),'summary':'R141/143解除R142条件：同原node12全46高度固定点+真实Robin DN使完整动量同，高频原迹同、唯一完整mean根同；一次高度常量/平面刚体规范配完整二jet。原内12..224+R18真∞尾与外11/10同g C²接合，far/cuff不改；未称0..9、整面嵌入或闭面。','result_entry':'## R145：原内尾与两外胞元的精确C²接合\n\n[完整迹、均值与二jet证明](results/R145-exact-inner-tail-two-cell-C2-gluing.md)。R141/143真实全cut解除R142条件，同原g与原∞尾接合到node10；独立far及单一cuff高度规范保留。'}]
sp=B/'queue-spec-r145.json';fresh(sp,json.dumps(spec,ensure_ascii=False,indent=2)+'\n');print('MANIFEST',sha(manifest))
