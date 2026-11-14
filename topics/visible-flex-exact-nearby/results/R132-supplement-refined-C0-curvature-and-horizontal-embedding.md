# R132 续篇：完整 C0 比较、曲率 10.367 与水平框架嵌入界

2026-11-13。

**本篇已执行结论。** 对 R132 的同一原始目标、同一真实腰分支、完整
η∈[−10^-9,10^-9]，新300闭盒的完整相关Taylor残差及R131 C0-only屏障
全部通过，覆盖[0,1/20]。真实末端零阶误差小于0.027567044，实际gap
大于0.19312757486；同一精确嵌入环带[-.05,.05]的主曲率绝对值小于
10.366510。只计水平位移的准确frame估计进一步给
φθ>0.2696679160、柱Jacobian>0.2902050414。

本篇没有将实际一阶导数的有限上界称为导数误差，没有由局部曲率上界
推出闭曲面的reach，也没有回写此前150盒的失败屏障。

## 1. 完整 C0 残差的准确输入

采用R130同一明确dyadic候选，75个分片径向七次多项式、完整512角
Fourier数据。每个候选分片再分4个闭盒，共300盒；所有盒留在一个
真正公共scalar germ内。物理闭角格4096、准确候选存储网1024。
非线性乘除在实际区间jet中进行，没有用1024网作截断Fourier乘积。

生产者 `fourfold_codazzi_residual_C0_taylor.py` 使用同一完整原始
primitive和全部无限尾、同一wholeη盒及R130高目标jets。
它以中心完整残差及一次导数支付整个闭矩形的二维二阶Taylor余项。
为延拓目的只要残差本身，故保留的归一化候选导数矩形是r≤3、θ≤3；
闭角格的场值另付θ≤5，完整残差矩形为r≤2、θ≤2。
这恰好支付R130 j=0的全部余项，包括混合rθ项。
没有对原目标或真实无限角补集作任何删减。

实际运行为1060.2661秒，全部300闭盒完整完成，failure=null。
新报告保持continuation_certified=false，因为producer只支付残差。
随后独立R131 v2消费者才认证继续存在。

## 2. 真正通过的逐盒 C0 屏障

R131使用实际特征比较
\[
D^+e_0\le A_0e_0+\rho_0,\qquad
A_0=\gamma D_1+|\beta|(1+3M_b^2)+2|\kappa|,
\quad M_b=\widehat M+1/16.
\]
每盒都保留严格仿射屏障余量，传递前盒终值而不重复膨胀整段误差。
完整检查给
\[
e_0(1/20)<0.027567043785<1/16,
\qquad\inf|p-q|>0.19312757486.
\tag{S.1}
\]
真实加权角梯度再由R131准确线性系统传播；实际一阶角导数全域小于
1322.433350，因此延拓不是将条件估计误当存在性。
此数是粗有限导数界，绝非候选C1误差。

消费者逐项核对producer/provider/candidate/object SHA、全η、完整角圆、
每盒实际germ、严格正微分余量及请求区间相等。旧完整150盒在row111
的1/16管门失败仍以独立报告保留；本篇读取的是新的300盒完整native。

## 3. 与 R132 不变矩形属于同一个实际解

R132从同一精确腰初值、同一固定目标独立证明全[0,1/20]的
p<0<q，并证明真Cauchy分支的经典唯一性与完整周期重建。
本篇C0比较也从该真实腰出发；局部唯一性及有限germ接续说明两套
证书指向同一分支。没有把两条不同背景的估计拼在一起。

在每个新闭盒中，若实际M≤M_i、实际gap≥g_i>0，则R132的准确符号给
\[
0<A\le k_i M_i,\qquad |B|\le k_i,\qquad |C|\le2k_i/g_i.
\tag{S.2}
\]
因此真实对称第二基本形式的Gershgorin界为
\[
\max(|\lambda_1|,|\lambda_2|)
\le\max(k_iM_i,2k_i/g_i)+k_i.
\tag{S.3}
\]
对全部300盒及整个η盒取最大值，实际有向结果为
\[
\boxed{\quad\max|\lambda_j|<10.366509967148<10.366510.\quad}
\tag{S.4}
\]
这改善R132原先14.000161的独立安全界。角导数误差并不参与(S.3)。

## 4. 只支付水平位移的真实框架估计

仍用同一实际框架及同一方向
\[
F_r=\sqrt E X,\quad
X_r=\sqrt E A n,\quad Y_r=\sqrt E Bn,\quad
n_r=-\sqrt E(AX+BY).
\]
初始X为竖直单位向量，所以Xh(0)=0。
置连续非减的有向积分类上界
\[
\mathcal X(r)=\int_0^r\sqrt E|A|,\qquad
\mathcal Y(r)=\int_0^r\sqrt E|B|.
\]
实际水平切向满足|Xh|≤min(1,𝓧)，于是
\[
|F_h-F_{0,h}|\le
\int_0^r\sqrt E\min(1,\mathcal X(t))dt=:\Delta_h(r).
\tag{S.5}
\]
一盒长度h，√E≤e、|A|≤a、盒初𝓧≤Xl时，可准确支付
\[
\Delta_{h,\mathrm{box}}
\le\min\{he,\ heX_l+\tfrac12h^2e^2a\}.
\tag{S.6}
\]
两项各自是全盒上界，所以取min合法。脚本按盒累积，不用右端节点
或浮点轨迹代替积分。

对法向的水平分量，|Yh|≤1给
\[
|(n_h)'|\le\sqrt E(|A|\mathcal X+|B|).
\]
这里𝓧的导数正是所取|A|的积分类majorant。因此
\[
\boxed{\quad |n_h-n_{0,h}|\le
\mathcal Y+\tfrac12\mathcal X^2=:N_h.\quad}
\tag{S.7}
\]
这不要求B保持某个号，也不将竖直法向变化收费到水平支撑中。
对水平Y仍用安全界|Yh−Y0h|≤𝓨。

同一R123/R128真实初始支撑>1/2、半径<13/10给
\[
\begin{aligned}
|F_h|&>1/2-\Delta_h,&|F_h|&<13/10+\Delta_h,\\
\det_h(F_h,Y_h)&>1/2-\Delta_h-(13/10)\mathcal Y,\\
F_h\cdot n_h&>1/2-\Delta_h-(13/10)N_h.
\end{aligned}
\tag{S.8}
\]
将它们代入R132完全相同的φθ和柱Jacobian恒等式，不改变材料角、
法向方向或固定φ高度单调的全局单射论证。

## 5. 实际全300盒几何结果

| 全域量 | 安全有向界 |
|---|---:|
| 完整位置位移 | <0.055564801 |
| 水平位置位移Δh | <0.003878694095 |
| 𝓧 | <0.139102042151 |
| 𝓨 | <0.051649059222 |
| 水平法向变化Nh | <0.061323748287 |
| 水平半径下界 | >0.49612130590 |
| 角分子det_h(Fh,Yh) | >0.42897752891 |
| 水平法向支撑Fh·nh | >0.41640043313 |
| 实际φθ | >0.2696679160 |
| 实际柱Jacobian | >0.2902050414 |
| 实际主曲率绝对值 | <10.366510 |

四项几何门全部实际通过。消费者明确检查R132的真符号/存在报告，
R131的真C0报告及其相应native，再核全部源SHA、同对象/中心/η盒、
相同准确区间及逐盒门。水平估计和全部方向另经独立代数审阅。

## 6. 固定文件与复现

- `scripts/fourfold_codazzi_C0_curvature_horizontal_frame.py`：`7e9c36c483f7f96caf14d50db47cdfb7885c7df18b06fe688183b27879314a5d`。
- `notes/2026-11-13-Codazzi-C0-Taylor-r005-v1-native.json.gz`：`780315ea1bc710e7e823a425dd9ff60833a1c11491ed385fd91b3968fd5ce26e`。
- `notes/2026-11-13-R131-C0-only-r005-refined-v1-native.json.gz`：`48d99904209e12ffeac60e64572ac515b5e8490e90f189e088fcf45c9acc43cd`。
- `notes/2026-11-13-R132-C0-horizontal-geometry-r05-native.json.gz`：`9eff9c2e20ac0f7bf309ba39416ce7194d1ddba6870fb43c5cf2bbac55dd04d6`。

源producer已在原compact失败记录提交中永久保存；本篇追加完整成功报告。
消费者可用新的输出路径复跑：
```bash
PYTHONPATH=/workspace/scratch/ac0d699811ad/python-deps \
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_codazzi_C0_curvature_horizontal_frame.py \
  --out /tmp/R132-C0-horizontal-geometry-r05-native.json.gz
```

下一批独立target-only producer正支付更远[0,1/5]的完整目标系数；它
不使用PDE候选，也不宣告该区间有解。真正扩展、跨根和正帽/regular闭合
仍须另付对应定理。当前局部曲率<12仅为全闭面几何预算准备一块输入，
不是reach、固定开帽或公共度量非全等族的最终结论。
