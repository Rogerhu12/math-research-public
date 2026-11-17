# 原真实首单元的共享 Cartesian 二jet重建

会话：`true_a_analysis`。本批仍固定原 `−.0781 H` 接受尾的第0个完整物理单元、同一尾参数、同一完整两端条件、M8和128点角求积。没有增大振幅，也没有改变物理尾。原有限射击解及实际单元恢复入口见父目录的 `actual_cell_notes.md` 和40文件 `actual_cell_manifest.json`。本目录只增加明确的连续代表和其采样审计。

## 数学定义

取统一径向坐标 `x=r_outer−r`。在每个已完成的物理h/p混合解节点，用不可变原momentum引擎独立恢复完整Cartesian位置、一阶和二阶导数，包含mean根和全部原表示模式。这个**后处理**在节点正Gram支上调用原引擎；此前的混合边值求解仍是完整全局系统，没有消去局部Gram。不能从本后处理推广到Gram奇点。

原独立开发使用同一零均值角相位原函数和居中平面位置。所有节点保留该共同框架，不对各stage另拟合刚体运动。外端checkpoint的momentum重标度已由原数据导出器按真实portRatio恢复；新节点转换使用

\[
 h_j=rwv_j,\quad p_j=w^2t_j,\quad
 Q_j=\sqrt2\,h_j/r^4,\quad
 \pi_j=\sqrt2\,r^4p_j/(\sqrt{12}\,\mu).
\]

因此在同一物理节点切换到相邻stage时，固定的是物理h/p。两侧实际Cartesian二jet的小差单独报告；每个接口明确选外侧stage内端的那一组字面数据，左右多项式都使用它。没有隐含平均。

### 已知背景与扰动

合理的代表保留原固定旋转背景

\[
 X_0(r,u)=(r\cos u,r\sin u,Z_0(r)),\qquad
 Z_0(r)=\int_{r_{\rm outer}}^r w(t)\,dt.
\]

对完整三维扰动的每个位置/一阶/二阶节点数据取128点离散Fourier系数，去掉Nyquist，保留所有 `−63,…,63` Cartesian频率。这不是只保留高度的8个模式。平面均值由共同居中规范固定为零；高度均值单独保留。把所得有限复数系数的实、虚部看成固定实常数，并对最后有限和取实部，便给出明确的三角多项式。

每个相邻径向节点之间，对各Cartesian Fourier系数取唯一五次Hermite多项式。设宽度为h，左端值/导数/二阶导数为y,d,q，右端为Y,D,Q，定义

\[
 e_0=Y-y-hd-\tfrac12h^2q,\quad
 e_1=D-d-hq,\quad e_2=Q-q.
\]

归一坐标t上的系数为

\[
 (y,hd,\tfrac12h^2q,
 10e_0-4he_1+\tfrac12h^2e_2,
 -15e_0+7he_1-h^2e_2,
 6e_0-3he_1+\tfrac12h^2e_2).
\]

两边使用同一节点二jet，故这些系数定义的实函数严格C²；角向是有限三角多项式，所以所有总阶数≤2的混合导数也连续。这是代数端点恒等式，不依赖采样接点误差为零。浮点实现另外报告端点恒等式的数值偏差。

### 完整mean与接口

写扰动mean为m(x)，其节点导数为

\[
 d_i=m_x(x_i)=-w_iL_{0,i},\qquad
 q_i=m_{xx}(x_i)=\partial_r(wL_0)(r_i).
\]

从m₀=0开始，用

\[
 m_{i+1}=m_i+\tfrac h2(d_i+d_{i+1})
                 +\tfrac{h^2}{12}(q_i-q_{i+1})
\]

规定全局节点位置。这是未舍入时对端点共享斜率/导数三次多项式的精确积分。代码只在构造结束把位置舍入到binary64，最终代表严格定义为这些字面位置及d、q的**五次**Hermite多项式；不把舍入后的曲线强称为精确四次。每个shooting接口只使用一次m值，不会重置mean高度。

### 背景的C²性及数值范围

这里的原物理背景是factory的积分定义，不是将自适应求积程序本身视为解析函数。在旧径向坐标ρ中，原w₀(ρ)是C¹；log过渡用S(t)=t³(10−15t+6t²)，满足S′(0)=S′(1)=0。cap及valley改正使用相同端点值与零端点一阶导数；外端的cut-preserving过渡也保持其原jet。

把原factory的正径向重参数写成

\[
 J=\frac{dr}{d\rho}
  =j_0(1-\chi)
   +\frac{\chi|w_{0,\rho}|}{\kappa(1+w_0^2)^{3/2}}
   +\frac{\chi\alpha\,b(\rho)}{1+w_0^2}.
\]

这里b(ρ)>0是 `closing_weighted_tail.mjs` 的正free-warp权重；它在每个cell两端严格取1，在相邻段匹配，使用同一S过渡。本支α>0、j₀>0、0≤χ≤1，所以J连续且严格正。于是逆坐标ρ(r)为C¹，w(r)=w₀(ρ(r))为C¹，Z₀'=w给出C²背景。`|w₀,ρ|`的尖点可能损害更高阶光滑性，但不损害这里所需的C²。原profile在stage中的r值由数值求积近似这些定义；本批没有给这些积分做区间余项认证，故后述数值是采样诊断，不能作为精确背景上的连续界。

## 已完成的对照

先把整个背景mean也作五次位置插值，uniform16结果为：metric `1.5983565e−5`、曲率 `11.6799463`、完整Cartesian张量 `2.1278741`。固定该解而保留精确背景后，三项变为 `3.0193898e−7`、`8.0401458`、`.0045470618`。这确认大部分首次恶化来自对已经知道的背景w进行额外低次插值。首次结果和其原源码一并保留。

一次指定的同g加密把每stage区间数16改为32；仍使用同M8、N128、原物理参数、完整边界和所有代数门，物理h/p混合BVP两次Newton接受。其根相对残差 `5.17195e−16`，ODE残差 `1.32854e−18`，minA `.00264208`，相对独立原动量流状态差 `9.38297e−6`。接着使用完全同一Cartesian重建。

|同一背景、同一M8|uniform16|uniform32|
|---|---:|---:|
|共享节点数|577|1153|
|metric采样最大值|3.0193898e−7|1.0782049e−7|
|实际曲率采样最大值|8.0401458|8.0400067|
|完整Cartesian张量采样最大值|.0045470618|.0082954392|
|实际Gauss与目标差|.0041214519|.0074670206|
|节点metric最大值|7.2742162e−8|7.2710529e−8|
|节点完整张量最大值|.0001759117|.0001758557|

每个径向小区间取5点，角向取256点。**完整张量恶化，故这一对照没有给出C²误差收敛。** 只有metric和曲率的采样数改善；固定M8的节点残差亦没有趋零。两层不能推出极限、连续严格曲率界、无限尾闭合或10%目标。

完整张量最坏点都位于raw segment7的w径向极值附近，uniform网格没有把原warp的关键尖点指定为节点。其余段分别记录，不把这些峰值删去。后续若检验关键点网格，必须使用同物理g并独立记录；本批不假设它会成功。

## 复现

本目录安装在已发布40依赖 `actual_cell` 目录下。新 `cartesian_c2_manifest.json` 固定本目录新源码，并列出所需父目录源码SHA；原40文件恢复仍由父目录manifest负责。所有轨迹、系数、角数组均生成到用户指定scratch。

1. 从原stage1的确切同向量延拓再生接受checkpoint，或显式传入已有的同参数checkpoint。
2. 调父目录 `export_actual_cell.mjs`，分别参数 `16 256 0 0 uniform`、`32 256 0 0 uniform`；若要复现旧16输出SHA及旧audit，16用 `cartesianFlag=1`。
3. 父目录 `probe_actual_cell.py --coordinates physical` 得到成功summary及NPZ。
4. 本目录 `prepare_shared_nodes.py --input CELL.json.gz --solution SOLVE.json --output NODES.json.gz`。
5. `node export_shared_cartesian_jets.mjs SOURCE_TOPIC NODES.json.gz ORIGINAL_CHECKPOINT JETS.json.gz 0.0001 4`。
6. `python build_shared_cartesian.py --input JETS.json.gz --out C2.json --angular 256 --background-height exact`。

`--background-height quintic`重现额外背景多项式对照。最早该对照的源码保留为 `build_shared_cartesian_polynomial_mean_v1.py`；随后只调整背景选项及避免数组视图的写法，没有改变该公式。原spatial引擎的平面rr使用记录的stage参数四阶差分步 `1e−4`；本批没有把这一数值jet误差当作区间界。C²代表由实际存储的节点jet定义，故其C²性并不要求该jet等于不可得的精确解jet。
