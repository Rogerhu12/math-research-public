# R87：实际有限 canonical 领口、物理多项式试解与完整源系数

2026-11-12，independent-audit。

**状态：完整证明，当前整个有限领口的连续角、径向和参数盒已实际通过。**
本篇直接使用 R83 同一公共参数盒、真正移动根和无限原函数。它不从根
jet 的值推断整个领口，也不要求在椭圆侧求一个未给存在性的 Cauchy 解。
完成报告含 178 个实际连续半 quarter 角区间，径向覆盖整个 (87.2)，
再由准确对称性补齐全圆和另一根。完整 Airy 矩、全 lag 聚合及最终
反馈 cutoff 尚须根据这些实际完成的系数界继续支付。

## 1. 同一个实际算子与固定物理领口

参数严格取
\[
 \delta_5=-7789843107295549/4611686018427387904,\qquad
 |\delta-\delta_5|\le1/2500000.
 \tag{87.1}
\]
令 \(t=t(\delta)\) 为 R83 同一根，正侧物理变量为
\(s=r-t\)。本篇实际计算的目标域为
\[
                 0\le s\le h,\qquad h=1/2048.
 \tag{87.2}
\]
整个真实根盒加上此段严格留在一个共同实际 scalar spline span 内；
原始及反射 spline 的准确 span 分别检查。较大的复盘只为这个多项式
germ 的 Cauchy 费用使用，不转授给跨 knot 的全域样条。

沿用 R83 全 \(\ell\) 口径、正 ground state \(Y=Y_z\) 和实际密度
\[
 Y\widehat P(Yu)=\operatorname{div}(B\nabla u),\quad
 B=\begin{pmatrix}
 \alpha&-\alpha q\\
 -\alpha q&\alpha q^2+\eta K_0
 \end{pmatrix},\qquad q=M/D.
 \tag{87.3}
\]
\(\alpha,\eta,q,K_0\) 都是当前真实非径向对象；正能量算子记为
\(P_g=-\operatorname{div}(B\nabla)\)。
以下 source 先指这个 grounded 物理密度源。若回到原始
\(\widehat P\)，必须按最后的精确式重新带回 \(Y\)。

## 2. 在物理变量中直接递推六阶坐标

负侧置 \(x=t-r\)，并记
\[
 \rho=1/1024,\qquad x=\rho z^2,\quad
 d(x,\theta)=\sqrt{\kappa\eta/\alpha},\quad
 Y_0'=d(0,\theta)^{-1}.
\]
负侧密度为
\(\alpha\bigl[\begin{smallmatrix}1&q\\q&q^2-xd^2\end{smallmatrix}\bigr]\)。
因此准确逆特征标签满足
\[
 (S_\pm)_z+
 [\,2\rho zq(\rho z^2,\theta)
       \pm2\rho^{3/2}z^2d(\rho z^2,\theta)\,](S_\pm)_\theta=0,
 \qquad S_\pm(0,\theta)=Y_0(\theta).
 \tag{87.4}
\]
在这个实际解析根 germ 中，普通流方程给局部真实标签。
系数只依赖 \(z^2\)，唯一性给
\(S_-(z,\theta)=S_+(-z,\theta)\)。

写 \(q(\rho w,\theta)=\sum q_jw^j\)、
\(d(\rho w,\theta)=\sum d_jw^j\)、
\(S_+=\sum S_nz^n\)。逐系数比较得完整有限递推
\[
 S_n=-\frac2n\left[
 \rho\!\!\sum_{j\ge0,\ k=n-2-2j\ge0}q_j\partial_\theta S_k+
 \rho^{3/2}\!\!\sum_{j\ge0,\ k=n-3-2j\ge0}d_j\partial_\theta S_k
 \right].
 \tag{87.5}
\]
这里仅用 \(\partial_\theta S_0=Y_0'\)，不需要先数值积分出 \(Y_0\)
的相位值。特别
\[
 S_1=0,\quad S_2=-\rho q_0Y_0',\quad
 S_3=-2\rho^{3/2}/3
 \tag{87.6}
\]
是准确恒等式；最后一个常数及其零角导数在程序中准确保持。

记 \(\mathcal T_5\) 为截到 \(w^5\) 的 Taylor 多项式。使用到 \(S_{13}\)
即明确给出
\[
\begin{split}
 H_5(w,\theta)&=-\frac3{2\rho^{3/2}}\sum_{j=0}^5S_{2j+3}w^j,
                  \qquad H_5(0)=1,\\
 \xi_6(x,\theta)&=\rho w\,\mathcal T_5(H_5(w,\theta)^{2/3}),
                  \qquad w=x/\rho,\\
 \phi_6(x,\theta)&=Y_0(\theta)+\sum_{j=1}^6S_{2j}w^j .
\end{split}
\tag{87.7}
\]
这些系数是实际根函数，不是将区间中点当成新的坐标定义。
它们与 R39 的准确 \((\xi,\phi)\) 具有相同的前六阶径向 jet。
根 germ 的局部解析性只用于证明这些有限恒等式；随后使用的坐标
是 (87.7) 明确写出的有限多项式。

正侧实际采用
\[
       y(s,\theta)=-\xi_6(-s,\theta),\qquad
       \phi(s,\theta)=\phi_6(-s,\theta).
 \tag{87.8}
\]
程序直接验证其整个实域的
\[
 y/s>0,\quad y_s>0,\quad \phi_\theta>0,\quad
 J=y_s\phi_\theta-y_\theta\phi_s>0.
 \tag{87.9}
\]
\(y/s\) 使用去掉准确零常数的多项式计算，绝不将包含零的 \(s\) 球
用于除法。若 (87.9) 在全域成立，则对每个 \(s\)，\(\phi\) 是
度数一的真圆图。在固定 \(\phi\) 上
\(dy/ds=J/\phi_\theta>0\)，故整个映射是 onto 其像的真实微分同胚；
其像是 \(0\le y\le b(\phi)\) 的正图域，固定角的每段径向线都留在像内。

## 3. 准确高度、完整势和源密度

设 \(D\Psi\) 为 (87.8) 的坐标导数矩阵。定义
\[
 A=\frac{D\Psi\,B(D\Psi)^t}{J},\quad
 \tau=A_{11}^{-1/2},\quad
 C=\tau^2 A,\quad E=C-\operatorname{diag}(1,y).
 \tag{87.10}
\]
程序单独验证 \(A_{11}>0\)；\(\tau\) 使用这个真实平方根，
不是另取一个未控制余项的 height Taylor 多项式。于是 \(E_{11}=0\)
准确成立，且
\[
 V=-\frac{\tau}{J}\operatorname{div}_{s,\theta}(B\nabla_{s,\theta}\tau).
 \tag{87.11}
\]
真实算子恒等式为
\[
 \boxed{\quad
 P_g(\tau U\circ\Psi)=\frac J\tau
 \left[-\partial_y^2-y\partial_\phi^2+V
                       -\operatorname{div}_{y,\phi}(E\nabla)\right]U\circ\Psi .
 \quad}
 \tag{87.12}
\]
它直接由变换后的弱二次型和乘子 Leibniz 恒等式证明，包含全部
零阶、第一阶和混合项。原始物理未知量是 \(w=Y\tau U\circ\Psi\)，
因而
\[
 \widehat P(w)=-\frac{J}{Y\tau}(P_{\rm can}U)\circ\Psi .
 \tag{87.13}
\]
源中的 `physical_source_factor` 在本程序明确表示 \(J/\tau\)，
即 (87.12) 的 grounded 物理密度因子；回到原始算子还须 (87.13)
的 \(Y^{-1}\)。R85 的同一整帽 form/contact 作用于 \(P_g\)，所以
将本篇 trial 送入 R85 时恰使用 \(J/\tau\)，不遗漏也不重复 \(Y\)。

六阶坐标匹配还给比 R53 所需更高的实际主部消失阶：
\[
                   E_{12}=s^6e_{12},\qquad E_{22}=s^7e_{22}.
 \tag{87.14}
\]
证明不依赖一次浮点相消。相对于准确 canonical 坐标，
\(\widetilde y=y+O(y^7)\)、\(\widetilde\phi=\phi+O(y^7)\)；
其 Jacobian 的两径向误差为 \(O(y^6)\)，两角向误差为 \(O(y^7)\)。
把 \(\operatorname{diag}(1,y)\) 按这个真实变换拉回，再除以准确的
第一主系数，交叉项为 \(O(y^6)\)，第二对角项减 \(\widetilde y\)
为 \(O(y^7)\)。根处 \(y/s=1\)，故得到 (87.14)。
对物理角有限次微分保持这些消失阶。

对
\[
 \partial_y=\frac{\phi_\theta\partial_s-\phi_s\partial_\theta}{J},\qquad
 \partial_\phi=\frac{-y_\theta\partial_s+y_s\partial_\theta}{J}
 \tag{87.15}
\]
还分别有
\((E_{12})_y=O(s^5)\)、\((E_{12})_\phi=O(s^6)\)、
\((E_{22})_\phi=O(s^7)\)。后一项使用
\(y_\theta=O(s^2)\)，不能将逆坐标角导数草率当成物理 \(\theta\)
导数。

## 4. 直接物理多项式 trial 保持同一根 Cauchy 数据

令 \(\bar v_i(\theta)=v_i(Y_0(\theta))\)，取
\[
\begin{split}
 B_+(s,\theta)&=-\bar v_0(\theta)
      +s\left[\bar v_1(\theta)/3-q_0(\theta)\bar v_0'(\theta)\right],\\
 C_+(s,\theta)&=\frac{s^2\bar v_0'(\theta)}{2Y_0'(\theta)}.
\end{split}
\tag{87.16}
\]
它们是物理 \(s\) 的明确多项式，避免在整个领口反求
\(Y_0^{-1}(\phi(s,\theta))\)。它们不是原 R53 多项式在体域上的
相同函数，但有完全相同且足够的根数据。因为
\(\partial_y|_0=\partial_s-q_0\partial_\theta\)，准确有
\[
 B_+(0)=-v_0,\quad (B_+)_y(0)=v_1/3,\quad
 C_+(0)=(C_+)_y(0)=0,\quad (C_+)_{yy}(0)=(v_0)_\phi .
 \tag{87.17}
\]
真实有限坐标和高度又给 \(V(0)=-v_0,V_y(0)=v_1\)。
因此采用任意明确、根附近等于 1 的径向 cutoff 后，非零输入列
\[
 c\lambda^{-1/3}e^{i\epsilon\lambda\phi}
 \left[(1+i\epsilon C_+/\lambda)\operatorname{Ai}(y\lambda^{2/3})
      +\lambda^{-4/3}B_+\operatorname{Ai}'(y\lambda^{2/3})\right]
 \tag{87.18}
\]
仍有 R53(53.32) 的准确根迹和通量。共根自伴剪切、真实 height/shear、
root 零模与 regular 平均端口继续使用 R83/R85 的同一框架。

## 5. 每一个 residual 项的真实径向阶

对一般真实 \(B_+,C_+\)，R53(53.28) 的代数恒等式仍然准确成立，
并不要求它们恰为 canonical 变量的多项式。记
\(L_+=-\partial_y^2-y\partial_\phi^2+V\)。Ai 与 Ai′ 两列中的
系数为
\[
\begin{split}
 D_B&=V-B_+-2y(B_+)_y+2y(C_+)_\phi,\\
 D_C&=(C_+)_y+y(B_+)_\phi.
\end{split}
\tag{87.19}
\]
由 (87.17)，\(V-B_+-2y(B_+)_y=O(s^2)\)、\(D_C=O(s^2)\)；
单独保留的 \(2y(C_+)_\phi=O(s^3)\) 不与前一项合成一个较粗的
二阶常数。完整四项为
\[
 c e^{i\epsilon\lambda\phi}
 \left[\lambda^{-1/3}D_B A
 -2i\epsilon\lambda^{-2/3}D_C A'
 +i\epsilon\lambda^{-4/3}(L_+C_+)A
 +\lambda^{-5/3}(L_+B_+)A'\right].
 \tag{87.20}
\]
\(A,A'\) 的自变量均为 \(y\lambda^{2/3}\)。下表记录程序分别计算、
并在后续 Ai 矩中保持的径向阶：

| 完整系数 | 至少含 \(s\) 的次数 |
|---|---:|
| \(V-B_+-2y(B_+)_y\) | 2 |
| \(2y(C_+)_\phi\) | 3 |
| \(D_C\) | 2 |
| \(-(C_+)_{yy}\) | 0 |
| \(-y(C_+)_{\phi\phi}\) | 3 |
| \(VC_+\) | 2 |
| \(-(B_+)_{yy}\) | 0 |
| \(-y(B_+)_{\phi\phi}\) | 1 |
| \(VB_+\) | 0 |

其余真实主部误差完整为
\[
 -2E_{12}U_{y\phi}-(E_{12})_yU_\phi
 -(E_{12})_\phi U_y-E_{22}U_{\phi\phi}-(E_{22})_\phi U_\phi .
 \tag{87.21}
\]
程序同时计算全部 \(B,C,B_y,B_\phi,B_{y\phi},B_{\phi\phi},
C_y,C_\phi,C_{y\phi},C_{\phi\phi}\)，以便逐项展开 (87.21)。
没有将 cross 项、角导数落在 phase 上的项、势乘子或普通源删去。

对固定物理 cutoff \(\chi(s)\)，最后还必须准确加入
\[
 P_g(\chi Q)=\chi P_gQ-2\nabla\chi\cdot B\nabla Q
                              -Q\,\operatorname{div}(B\nabla\chi).
 \tag{87.22}
\]
本篇的连续系数覆盖本身没有替 cutoff 选择、其导数和这一真实支持
区间的 Ai 指数费用自动付款。

## 6. 无除零的连续系数预算

对 (87.14)、(87.19) 或表中任意已证明消失 \(k\) 阶的实际函数 \(f\)，
Taylor 的准确积分式给
\[
 \partial_\theta^j\frac{f(s,\theta)}{s^k}
 =\frac1{(k-1)!}\int_0^1(1-u)^{k-1}
             \partial_s^k\partial_\theta^j f(us,\theta)\,du .
 \tag{87.23}
\]
所以全域 \(|\partial_s^k\partial_\theta^j f|\) 上界除以 \(k!\)
即控制商，包括根本身；\(k=0\) 直接取实际函数。程序记录的正是这些
已除阶乘的 sup。若径向用了多个 slab，必须先取所有 slab 的最大值，
不能把只覆盖外部 slab 的第 \(k\) 阶导数误当整个从根到该点的商界。

R47 在固定物理 \(s\) 的真正角坐标上使用全 lag。若
\(\psi=q\phi,\ q=2\pi/\ell\)，则该切片上的导数是
\[
 \partial_\psi=(q\phi_\theta)^{-1}\partial_\theta,\quad
 |\partial_\psi^2 f|
 \le q_-^{-2}\left(
       \phi_{\theta,-}^{-2}|f_{\theta\theta}|
       +\phi_{\theta,-}^{-3}|\phi_{\theta\theta}|\,|f_\theta|\right).
 \tag{87.24}
\]
它与 (87.15) 的固定 canonical \(y\) 导数不同，程序分开携带。
四重输入物理频率为 \(4q|j|\)；R85/R34 之间的 \(16q^2\) 换算仍保留。

## 7. 真无限对象、有限 Taylor 移心与余项

实现位于
`scripts/fourfold_phase_canonical_collar_finite.py` 和
`scripts/fourfold_phase_canonical_collar_centered_cover.py`。
根处先取得 Q512 的有限 Fourier 原函数及其前 80 个径向 Taylor 系数，
并支付 R52 的完整无限 alias/tail。角导数随后用准确柱坐标恒等式
\(F_\theta=aT-J_{\rm rot}F\) 生成，未对有限 primitive 直接作角微分。

为避免对每个体盒重新进行宽区间 Fourier 相消，直接平移根处的真实
径向 Taylor 多项式，并逐个局部 Taylor 系数付整个解析余项。
设根外盘半径 \(R\)，完整函数模数 \(M\)，保留次数 \(0,\ldots,P-1\)，
平移后中心距根不超过 \(b<R\)。记 \(q_R=b/R\)。第 \(j<P\) 个以
尺度 \(\rho\) 归一化的局部系数遗漏量不超过
\[
 M(\rho/R)^j
 \sum_{a=0}^j\binom Pa
       \frac{q_R^{P-a}}{(1-q_R)^{j-a+1}}.
 \tag{87.25}
\]
这是 \(\sum_{n\ge P}\binom nj q_R^{n-j}\) 的准确几何导数公式，
不是把有非零常数的 Taylor 合成当成无损。已知根系数的无限原函数
费用 \(\varepsilon(\rho/R)^n\) 平移后另付
\[
              \varepsilon(\rho/R)^j(1-q_R)^{-j-1}.
 \tag{87.26}
\]
对 \(E=\langle|F_r|^2\rangle\)，先加上真实 \(E\) 的逐系数无限费用，
再平移，并用实际较小的 \(R_E\) 和完整 \(M_E\) 支付 (87.25)。
之后才形成真实 \(K_0\)。所有参数仍共享同一个实际仿射球及各自
真正根；准确 \(K_0(t)=0\) 只用于根处常数，所有更高真实系数保留。

从有限多项式平移得到的未知高阶并不补零。唯有 (87.7) 本来定义成
六阶多项式的坐标，才准确具有零的更高多项式系数。函数分支、原始
对象、root 输入、原函数依赖及源码 SHA 均写入实际报告。

### 7.1 有限三角相位的中心展开

直接把每个 \(e^{4im\theta}\) 独立扩成一个矩形会破坏 mode 间的
真实相消。完成的运行因此使用 centered 引擎：对每个实际相位的
归一化角导数 \(f^{(j)}/j!\)，先在角盒中心 \(z_c\) 准确求和，再
以 \(z-z_c\) 展开到八阶。对于径向系数为 \(b_{im}\) 的一个实际
三角 mode，复矩形半径为 \(h_{\rm re},h_{\rm im}\)，
\(d=(h_{\rm re}^2+h_{\rm im}^2)^{1/2}\)，该展开的遗漏模数至多
\[
 |b_{im}|\,e^{4m(|\operatorname{Im}z_c|+h_{\rm im})}
       \frac{(4m)^{j+9}d^9}{j!\,9!}.
 \tag{87.27}
\]
这是复线段 Taylor 积分余项。所有 mode 的费用逐个相加，既不把
区间参数改成中点，也不把盒上的真实函数换成中点函数。实角运行
最后按真实共轭性取实部。该改进只改变包络方式；根系数、有限
坐标、Cauchy 费用和真实算子均未改变。

实现复用
scripts/fourfold_phase_root_potential_complex_strip.py 的相位函数，
通过 scripts/fourfold_phase_canonical_collar_centered.py 接入本篇
真实物理引擎。报告明确保存这两个额外依赖的 SHA。较早的非中心
包络只留下未完成的诊断记录，没有与新运行拼接成完成证书。

## 8. 已完成的实际全域系数门与尚未冒称的算子界

局部真有向诊断已核对：在 \(\theta=\pi/16,s=0\)，
\(V=-v_0,V_y=v_1\) 与 R83 独立公式相容；全部应消失的主部和
\(D_B,D_C\) 根 jet 包含准确零。这个检查只用于发现实现错误，
消失阶的证明是上述代数推导。

连续角程序逐个准确 Fraction 角区间及径向 slab 计算 (87.9)、
完整势和 §5 各项，再检查无缝覆盖。反射
\(\theta\mapsto\pi/2-\theta\) 给 \(y,\tau,V,B_+\) 偶，
\(\phi\mapsto\ell/4-\phi\)、\(C_+\) 奇；各 jet 的绝对界由真正
前半 quarter 推得另一半。负径向根由同一个实际球面反射给出。

运行命令为

```bash
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python -u scripts/fourfold_phase_canonical_collar_centered_cover.py \
  --out notes/2026-11-12-actual-finite-canonical-collar-centered-cover.json.gz
```

完整运行共 228 次尝试、178 个接受格，无失败或遗漏格，实际耗时约
478 秒。每格包括整个准确径向段和同一个完整参数盒。仍须以这些真实
系数付 R47 的 Ai 矩、全部 Fourier lag、真实切片角图及
(87.22)，再使用 R85 的完整 contact \(<800\) 和同 frame 酉性。
只有这些合并后才给实际总余项和可计算 cutoff；有限低块继续保留
真正 root mean、regular \(\lambda\) 与全部源/重建条件。

### 8.1 当前整个领口的安全数值

独立的 scripts/fourfold_phase_canonical_collar_aggregate.py 再检查准确
无缝覆盖及所有导数界有限，生成
notes/2026-11-12-actual-finite-canonical-collar-aggregate.json。
全部 178 格重新取最坏有向端点后，可以统一取
\[
 \begin{gathered}
 .98306302<y/s<1.00270771,\qquad
 .96567150<y_s<1.00576591,\\
 .055953798<\phi_\theta<.288068627,\qquad
 .054301412<J<.288570210,\\
 .399655262<A_{11}<.747278640,\qquad
 1.15680115<\tau<1.58182063,\\
 .042051723<J/\tau<.203668850.
 \end{gathered}
 \tag{87.28}
\]
这些是整个连续物理领口和全部实际参数的界，不是有限射线上的
样本。它们特别支付有限坐标的全域正性及真正物理源因子。

为显示本篇实际源预算的当前尺度，下表是
\(\sup|\partial_\theta^j f/s^k|\) 的向外放宽上界，\(j=0,1,2\)。
表中 \(k\) 是已证明的根消失阶，来自 (87.23) 的积分式；没有在
包含零的区间上作数值除法。

| \(f\) | \(k\) | \(j=0\) | \(j=1\) | \(j=2\) |
|---|---:|---:|---:|---:|
| \(D_B-2yC_\phi\) | 2 | \(8.547\,10^{10}\) | \(3.062\,10^{13}\) | \(1.454\,10^{16}\) |
| \(2yC_\phi\) | 3 | \(1.298\,10^9\) | \(2.574\,10^{11}\) | \(7.229\,10^{13}\) |
| \(D_C\) | 2 | \(4.564\,10^8\) | \(9.707\,10^{10}\) | \(2.479\,10^{13}\) |
| \(-C_{yy}\) | 0 | \(7.087\,10^5\) | \(1.416\,10^8\) | \(3.865\,10^{10}\) |
| \(-yC_{\phi\phi}\) | 3 | \(1.705\,10^{12}\) | \(4.978\,10^{14}\) | \(1.692\,10^{17}\) |
| \(VC\) | 2 | \(5.172\,10^{10}\) | \(2.092\,10^{13}\) | \(1.117\,10^{16}\) |
| \(-B_{yy}\) | 0 | \(1.455\,10^8\) | \(2.154\,10^{10}\) | \(6.305\,10^{12}\) |
| \(-yB_{\phi\phi}\) | 1 | \(1.734\,10^9\) | \(3.622\,10^{11}\) | \(1.047\,10^{14}\) |
| \(VB\) | 0 | \(4.925\,10^8\) | \(1.128\,10^{11}\) | \(4.183\,10^{13}\) |
| \(E_{12}\) | 6 | \(1.047\,10^{14}\) | \(6.006\,10^{16}\) | \(4.036\,10^{19}\) |
| \(E_{22}\) | 7 | \(9.405\,10^{15}\) | \(5.965\,10^{18}\) | \(4.454\,10^{21}\) |

这些界完整但有明显的区间相消损失；尤其高角导数栏不代表实际
导数的典型量级。不能仅凭表格完成就宣称已有可计算的反馈
cutoff。正帽压缩高角体源已另由 R89 的真实能量给出较小的
\(N\) 相关费用；仍须保留完整边界延拓和低高 Schur 耦合。
