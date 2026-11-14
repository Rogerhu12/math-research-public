# R95：同一 r=1/4 接口的完整外帽延拓与互补能量通量界

2026-11-12，reproduce-newton。

本篇使用 R88 当前有限核心真正接到的物理接口 \(c=1/4\)，
不是转折根 \(r=t\)。实际对象是显式对称化的准确仿射点
\[
 \delta_5=-7789843107295549/4611686018427387904 .
 \tag{95.1}
\]
局部系数计算在这个点上完成；引用全域正帽报告时，只使用其
已证参数盒确实包含该点的结论。这里的自然边界空间是物理
\(H^{1/2}\)，不转授 R94 真根处的 \(H^{1/3}\) 常数。

**已付范围：** 同一接口上方一个完整短窗的真实全角系数界，
完整未压缩外帽的延拓及能量型 contact 常数，全部 regular 均值槽，
以及从完整 primal/dual gap 到全边界通量误差的定理。
R88 的整个 body 能量积分完成之前，本篇不填写实际 gap 数值，
也不声称已经验证完整反馈逆。

## 1. 同一外帽 form 与准确端口

令 \(R=25/8\)。完整外帽由实际 body、自然接合和 R74 真无限尾组成：
\[
 b(u,v)=\int_c^R\langle B(r,\theta)\nabla u,\nabla v\rangle\,dr
       +\langle\Gamma_Hu_R^\perp,v_R^\perp\rangle .
 \tag{95.2}
\]
角内积采用 Fourier 平均内积；物理模为 \(e^{4ik\theta}\)。
换成所有模都归一化的 \(L^2(d\theta)\) 坐标时，矩阵不变，
mean 输入和输出必须一起换算。\(B\) 正是 R88 的 grounded
物理密度，不是未带 Jacobian 的坐标复合系数。

端口为
\[
 H_c(a,\xi)(c,\theta)=a(\theta),\qquad
 \operatorname{mean}_{\theta}H_c(a,\xi)(R,\theta)=\xi .
 \tag{95.3}
\]
regular 端的其余模式服从同一个真正 \(\Gamma_H\) 条件。
\(\Gamma_H1=0\) 只说明常数 form 槽为零；\(\xi\) 及其共轭通量
\(\lambda\) 始终存在。固定 (95.3) 后，真实调和延拓在这个完整
正 form 中最小化能量。体内没有 Fourier 投影。

写 \(a=\sum a_ke^{4ik\theta}\)，采用等价但明确的范数
\[
 \|a\|_{X_c}^2=|a_0|^2+\sum_{k\ne0}|4k|\,|a_k|^2,\qquad
 \mathcal X_c=X_c\oplus\mathbb C_\xi .
 \tag{95.4}
\]
输出空间是相应的 \(H^{-1/2}\oplus\mathbb C_\lambda\)。

## 2. 完整未压缩帽的短窗高迹延拓

实际闭窗为
\[
 [c,c+d]=
 \left[\frac14,\frac{2448832297382707}{9007199254740992}\right],
 \qquad d=\frac{197032483697459}{9007199254740992}.
 \tag{95.5}
\]
同一真实对象上的连续全角系数计算给
\[
 0<B(r,\theta)\le M_e I,\qquad M_e<0.302002445 .
 \tag{95.6}
\]
程序在每个真实共同 scalar span 的闭子区间上计算完整无限
primitive 和真实 phase，按实角网格间隙的一致区间包络覆盖整个
圆；它不是只检查节点。正性由真实 \(\alpha,\kappa\) 的正下界
支付，矩阵上界由每个角格的 Gershgorin 界给出。

给定只有 \(|k|>N\) 的物理边界迹，取
\[
 Ea(r,\theta)=\sum_{|k|>N}
       \left(1-\frac{r-c}{h_k}\right)_+a_ke^{4ik\theta},
 \qquad h_k=\min\{d,|4k|^{-1}\}.
 \tag{95.7}
\]
这是完整外帽的合法 \(H^1\) 竞争函数。它在短窗之外为零，
regular 平均值为零，尾 form 也为零。使用 (95.6)，再对完整
物理 Fourier 级数应用 Parseval，
\[
 b(Ea,Ea)
 \le M_e\sum_{|k|>N}
       \left(\frac1{h_k}+\frac{|4k|^2h_k}{3}\right)|a_k|^2.
 \tag{95.8}
\]
令 \(\lambda_N=4(N+1)\)、
\(z_N=\min\{d\lambda_N,1\}\)。函数 \(z^{-1}+z/3\) 在
\(0<z\le1\) 上递减，因此
\[
 \boxed{\quad
 b(H_c(a,0),H_c(a,0))
 \le E_N\|a\|_{\dot H^{1/2}}^2,\qquad
 E_N=M_e(z_N^{-1}+z_N/3).
 \quad}
 \tag{95.9}
\]
高频条件仅施加在入口迹上。实际最小化解可以产生所有低体模，
这些效应没有删除，也没有用压缩高体逆替代真实解。

## 3. 用同一闭窗支付 regular 均值延拓

将闭窗划分为已付区间 \(I_i\)，长度为 \(d_i\)，令准确数
\(A_i>0\) 满足
\[
 B_{11}(r,\theta)\le A_i\quad(r\in I_i,\ \theta\in S^1).
 \tag{95.10}
\]
这些 \(A_i\) 是保存的有向 binary64 上端点，作为准确有理数使用。
定义
\[
 J=\sum_i d_i/A_i,\qquad e(c)=0,\qquad
 e'(r)=\frac1{J A_i}\quad(r\in I_i),\qquad
 e(r)=1\quad(r\ge c+d).
 \tag{95.11}
\]
于是 \(e\) 准确连续，\(e(c+d)=1\)，并且
\[
 b(e,e)\le\sum_i A_i d_i/(J A_i)^2=J^{-1}.
 \tag{95.12}
\]
它在外段是常数，故实际 graft 与无限尾不产生额外能量。
分段导数不连续不妨碍 \(e\in H^1\) 的竞争函数资格。
这不把它当作经典调和解或散度零通量。

另一合法竞争函数是整个有限外帽上的线性函数
\((r-c)/(R-c)\)。R69/R74 的同一真实 shear form 全域上界 \(M_g\)
给它的能量不超过 \(M_g/(23/8)\)：角无关函数在实际 shear 中仍
角无关，密度已经在该 form 内。因此可取
\[
 E_\xi=\min\{J^{-1},\,8M_g/23\},\qquad
 b(H_c(0,\xi),H_c(0,\xi))\le E_\xi|\xi|^2.
 \tag{95.13}
\]
R88 全部 primal 能量完成后，其准确 \(\xi\) 列能量还可以进一步
减小 \(E_\xi\)，但不能在积分尚未完成时使用浮点对角元。

常数函数准确给
\[
 H_c(a_0,\xi)=a_0+(\xi-a_0)H_c(0,1)
 \quad\hbox{当入口仅含常数时}.
 \tag{95.14}
\]
所以 regular 槽与入口零模保持耦合，而非删去其中一个。利用
\(|\xi-a_0|^2\le2(|a_0|^2+|\xi|^2)\)，再对能量内积用
Cauchy--Schwarz，得到
\[
 b(H_c(a,\xi),H_c(a,\xi))
 \le(E_0+2E_\xi)\|(a,\xi)\|_{\mathcal X_c}^2.
 \tag{95.15}
\]
若入口只含 \(|k|>N\)，则相应费用是 \(E_N+E_\xi\)。

## 4. 任意完整能量型源的 contact

设线性泛函 \(\ell\) 满足
\[
 |\ell(v)|\le\eta\,b(v,v)^{1/2}.
 \tag{95.16}
\]
它可以来自体弱通量，也可同时包含非均值 Robin 端残差；这两部分
须在同一个能量对偶 norm 中完整支付。由 (95.9)、(95.13)、
(95.15)，完整未压缩 contact 满足
\[
 \|K\ell\|_{\mathcal X_c^*}\le\sqrt{E_0+2E_\xi}\,\eta ,
 \tag{95.17}
\]
\[
 \|\Pi_{>N}K_{\rm left}\ell\|_{\dot H^{-1/2}}
       \le\sqrt{E_N}\,\eta,\qquad
 |K_{\rm reg}\ell|\le\sqrt{E_\xi}\,\eta .
 \tag{95.18}
\]
同时保留这两个输出时，常数为 \(\sqrt{E_N+E_\xi}\)。
这里 \(\Pi_{>N}\) 是 \(r=c\) 的物理 Fourier 投影。
它不是 R92 的 canonical 角投影，也不是在体内压缩方程。

## 5. 完整 primal/dual gap 直接控制全部 DN 输出

对 R88 的有限入口向量 \(g\)，令 \(u_g\) 为真正完整帽解，
\(V_g\) 是保存的准确 admissible 有限试函数，\(j_g=(p_g,q_g)\)
是保存的准确散度零通量。regular 平均通量 \(p_{g,0}\) 不设为零。
令
\[
 \mathcal U_g=
 \big(B^{1/2}\nabla u_g,\ \Gamma_H^{1/2}u_{g,R}^{\perp}\big),\qquad
 \mathcal J_g=
 \big(B^{-1/2}j_g,\ -\Gamma_H^{-1/2}p_{g,R}^{\perp}\big).
 \tag{95.19}
\]
第二项的负号与真正 Robin 条件
\(p_R^\perp+\Gamma_Hu_R^\perp=0\) 一致。分部积分给
\[
 \langle\mathcal J_g,\mathcal U_h\rangle
 =-\langle p_{g,L},h_L\rangle+\overline{p_{g,0}}\,\xi_h.
 \tag{95.20}
\]
对 \(h=g\)，这就是 R88 的 \(L(j_g,g)\)，并由能量最小化得到
\[
 \|\mathcal U_g-\mathcal J_g\|^2
 =b(u_g,u_g)-2\Re L(j_g,g)+D(j_g)
 \le E(V_g)-2\Re L(j_g,g)+D(j_g).
 \tag{95.21}
\]
假定完整真能量已经给出
\[
 E(V_g)-2\Re L(j_g,g)+D(j_g)\le\Delta\|g\|_2^2 .
 \tag{95.22}
\]
右侧包括全部 body、自然 graft、真无限尾及所有数值误差。
只有部分径向区间的 gap 不能代入此式。

准确 dual 边界输出为
\[
 d_jg=(-p_{g,L},p_{g,0}) .
 \tag{95.23}
\]
它在当前内部模式 \(M=16\) 之外准确为零。其与完整真 DN 的差
对任意边界测试 \(h\) 的配对是
\(\langle\mathcal U_g-\mathcal J_g,\mathcal U_h\rangle\)。
故 (95.17)–(95.18) 给
\[
 \boxed{\quad
 \|(S_c-d_j)g\|_{\mathcal X_c^*}
 \le\sqrt{E_0+2E_\xi}\sqrt{\Delta}\,\|g\|_2 .
 \quad}
 \tag{95.24}
\]
对所有 \(N\ge16\)，由于 \(d_j\) 的高左迹准确为零，
\[
 \boxed{\quad
 \|\Pi_{>N}S_cg\|_{\dot H^{-1/2}}
 \le\sqrt{E_N\Delta}\,\|g\|_2 .
 \quad}
 \tag{95.25}
\]
regular 通量误差同样有 \(\sqrt{E_\xi\Delta}\) 界。
在 R88 的矩阵口径中，\(L(j_g,h)=g^*Th\)，所以
保留输出行上的 \(d_j\) 是 \(T^*\)，不能误写成 \(T\)。
新报告保存完整 34×10 dual 边界矩阵，而不只保存其 10×10 压缩。

## 6. 实际输入、重放与尚欠部分

本次 38 个闭格全部通过，无未解决子区间。完整实算为 8.40 CPU
秒；所有费用保留在报告中。安全放宽后的实际常数为
\[
 E_\xi<6.745394,\qquad
 \sqrt{E_\xi}<2.597190,\qquad
 \sqrt{E_0+2E_\xi}<4.117166 .
 \tag{95.26}
\]
局部逐格 mean 延拓将先前全域线性 ramp 的能量上界
\(51.118435\) 降到 (95.26)，未改变真实参数或端口。

| 物理入口高切 \(N\) | 完整高左迹 contact \(\sqrt{E_N}\) | 同时保留 regular 通量 |
|---:|---:|---:|
| 0 | 1.860179 | 3.194630 |
| 4 | 0.856933 | 2.734909 |
| 16 及以上 | 0.634563 | 2.673587 |

第一行仍不含入口零模；所有入口模式和 regular 一起使用 (95.26)
的 \(4.117166\)。表中是乘 \(\eta\) 或 \(\sqrt\Delta\) 的常数，
不是尚未完成的实际完整 DN 误差数值。

源为 scripts/fourfold_phase_cut_cap_lift.py，报告为
notes/2026-11-12-actual-quarter-cut-cap-lift.json。
它逐一核对同一对象、准确 trial、完整首单元分割、全域参数包含、
closed exterior 输入和源 SHA。所有真实 primitive 尾都进入闭格；
实角连续覆盖使用已有 native 网格间隙包络，不以节点间看起来
平滑作为证明。

~~~sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python scripts/fourfold_phase_cut_cap_lift.py \
  --out notes/2026-11-12-actual-quarter-cut-cap-lift.json
~~~

完整短窗常数是直接数值输入。完整 \(\Delta\) 将由
fourfold_phase_cap_energy_collect.py 在全部 body 完成后给出
\[
 \Delta\le
 \|\widehat E-T-T^*+\widehat D\|_2+\epsilon_E+\epsilon_D.
 \tag{95.27}
\]
它与有限压缩中心的半径是两个不同量。当前理论不把
\(\sqrt\Delta\) 的全部输出界当作某个最终 Schur 逆，也不把本接口
直接移到真正转折根。负侧需使用已证的真实反射及正确 height/
通量方向；canonical 接线仍须保留 R83/R92 的完整转换。
