# R93：实际物理高角整帽的 Agmon 衰减与远端完整源 contact

2026-11-12，independent-audit。

**状态：完整证明，实际 55 格领口和 R90 的完整正帽常数已支付。**
本篇在同一个物理 Fourier 高角限制问题上给远根源的严格衰减，
保留完整真实 regular Robin form。权只依赖径向变量，根处为零，
在 regular 端为常数，因此没有删掉边界项或产生角投影交换项。
全部低体、低根和 regular 均值槽仍须留在全 Schur 中。

## 1. 同一完整限制实现

取 R89/R90 公共准确参数盒
\[
 \delta_5=-7789843107295549/4611686018427387904,\qquad
 |\delta-\delta_5|\le1/2500000 .
 \tag{93.1}
\]
物理坐标 \(s=r-t(\delta),\theta\) 的完整正 form 是
\[
 b(u,v)=\int_0^L\!\!\int
   \alpha Du\,\overline{Dv}+\eta K_0u_\theta\overline{v_\theta}
       +\langle\Gamma_Hu(L),v(L)\rangle,\qquad
 D=\partial_s-q\partial_\theta,\quad L=25/8-t.
 \tag{93.2}
\]
这里 \(\Gamma_H\) 是同一实际 R74 无限尾给出的正自伴 Robin 算子；
没有用理想尾替换。设 \(P_N\) 为物理四重模 \(|k|>N\) 的投影，
\(\lambda_N=4(N+1)\)，并在整个体域限制 \(P_Nu=u\)。

由 R89/R90，
\[
 b(u,u)\ge\kappa_N\|u\|_2^2,\qquad
 b(H_Na,H_Na)\le E_N\|a\|_{X_N}^2,\qquad
 X_N=|D_\theta|^{1/3}P_NL^2.
 \tag{93.3}
\]
\(H_Na\) 在整个真实正帽上满足高角弱调和、根迹 \(a\) 和真实
regular Robin 条件；不在一个内部人工切口追加条件。
R90 记
\[
 C_N=\sqrt{E_N/\kappa_N},\qquad
 \|K_Nf\|_{X_N^*}\le C_N\|f\|_2,\qquad K_N=-H_N^* .
 \tag{93.4}
\]
原始根零模、regular \(\xi,\lambda\) 和全部低高 cross 不在这个
限制问题中被反演或删除，仍属于完整 Schur 系统。

## 2. 来自真实格的一个明确权

R66 的同一族连续领口给
\[
 K_0(t+s)\ge\kappa_c s,\qquad
 \kappa_c>14.3310205042362,\qquad
 l=1/4-t>.0116031248790358.
 \tag{93.5}
\]
对第 \(i\) 个实际物理径向格，记该格对全部角和参数已经支付的
\(\alpha\le A_i,\ \eta\ge e_i>0\)。全 55 格准确覆盖实际领口。
取
\[
 \sigma=\frac{1140554620}{10^9}=1.140554620,\qquad
 l_0=\frac{29}{2500}=.0116 .
 \tag{93.6}
\]
程序逐格以有向算术证明
\[
 \sigma^2<
       \min_i\frac{\kappa_c e_i}{2A_i},
 \qquad
 \min_i\frac{\kappa_c e_i}{2A_i}
       >1.3008648429141129,\qquad l_0<l.
 \tag{93.7}
\]
几何报告的 binary64 端点按其准确二进制有理数读入，
不是把十进制显示当作未经检查的方向舍入。

定义在整个真实 \(0\le s\le L\) 上的径向权
\[
 \boxed{\quad
 \psi_N(s)=\frac23\sigma\lambda_N\min\{s,l_0\}^{3/2}.
 \quad}
 \tag{93.8}
\]
它在根处准确为零，在 \(s\ge l_0\) 为常数；只需 Lipschitz
正则性。特别 regular 端权是与角无关的常数，和完整
\(\Gamma_H\) 准确交换。

对每个物理截面，高角 Poincaré 给
\(\lambda_N^2\|v(s)\|_2^2\le\|v_\theta(s)\|_2^2\)。
因此在相应真实格中，(93.7) 保证
\[
 \begin{split}
 \int\alpha|\psi_N'|^2|v|^2\,d\theta
 &\le A_i\sigma^2\lambda_N^2s\,\|v\|_2^2\\
 &\le\tfrac12e_i\kappa_cs\,\|v_\theta\|_2^2
 \le\tfrac12\int\eta K_0|v_\theta|^2\,d\theta.
 \end{split}
 \tag{93.9}
\]
在 \(s>l_0\) 左边为零。这里使用格上的 \(\eta\) 下界和
\(\alpha\) 上界，未把一个变系数加权角 Poincaré 不等式免费使用。

## 3. 保留真实端点的准确加权能量恒等式

令 \(u=H_Na,\ w=e^{\psi_N}u\)。因权径向，
\(P_Nw=w\)，并且
\[
 (e^{2\psi_N}-1)u
 \tag{93.10}
\]
是合法的高角零根迹 test function。它在 regular 端无需为零：
那里使用的是同一个真实自然 Robin form。弱调和性给
\[
 b(u,e^{2\psi_N}u)=b(u,u).
 \tag{93.11}
\]
直接展开 \(D(e^\psi u)=e^\psi(Du+\psi'u)\)，
以及完整 Robin 项，得到精确式
\[
 \boxed{\quad
 b(w,w)=b(u,u)+\int\alpha|\psi_N'|^2|w|^2.
 \quad}
 \tag{93.12}
\]
复函数时对中间式取实部。Robin 贡献是准确
\(e^{2\psi_N(L)}\langle\Gamma_Hu(L),u(L)\rangle\)，已在
两边同一个 form 内，并没有消失。

由 (93.9)，最后一项不超过 \(b(w,w)/2\)，所以
\[
 b(e^{\psi_N}H_Na,e^{\psi_N}H_Na)
          \le2b(H_Na,H_Na)\le2E_N\|a\|_{X_N}^2.
 \tag{93.13}
\]
整个证明不要求 \(P_N\) 与 \(q,\alpha,\eta\) 交换；
唯一使用的交换是 \(P_N\) 与径向标量权。
有限长度、根迹和 regular 端全部保留。

## 4. 远根体源及能量型源

由 (93.3)、(93.13)，对 \(d\ge0\)，
\[
 \|1_{s\ge d}H_Na\|_2
 \le\sqrt2\,C_N e^{-\psi_N(d)}\|a\|_{X_N}.
 \tag{93.14}
\]
与未加权界取较小者，并对偶，便得实际完整限制帽的远根体源
\[
 \boxed{\quad
 \|K_N f\|_{X_N^*}
 \le C_N\min\{1,\sqrt2e^{-\psi_N(d)}\}\|f\|_2,
 \quad\operatorname{supp}f\subset\{s\ge d\}.
 \quad}
 \tag{93.15}
\]
源可以有全部物理角模；高角解与 test 的配对准确取其高分量，
但全问题中的低源并未因此删除。

还可以保留源的散度形式，避免对源系数作一次不必要的角导数。
设弱源泛函
\[
 \ell_F(v)=\int F\cdot\overline{\nabla v},\qquad
 \|F\|_{\mathcal E^*}:=\|B^{-1/2}F\|_2,
 \quad
 B=\begin{pmatrix}\alpha&-\alpha q\\-\alpha q&\alpha q^2+\eta K_0\end{pmatrix}.
 \tag{93.16}
\]
定义相应 generalized contact 为
\(\langle K_N^{\rm div}F,a\rangle=-\ell_F(H_Na)\)。
若要把它写成普通源 \(-\operatorname{div}F\)，必须带回其实际
边界法向负荷；当 \(F\) 支撑在内部时这两种写法准确相同。

由 \(\nabla u=e^{-\psi}(\nabla w-\psi'w\,e_s)\)，
(93.9)、(93.13) 给
\[
 \|1_{s\ge d}B^{1/2}\nabla H_Na\|_2
 \le(1+\sqrt2)\sqrt{E_N}\,e^{-\psi_N(d)}\|a\|_{X_N}.
 \tag{93.17}
\]
这里先用
\(\|B^{1/2}\psi'w\,e_s\|\le b(w,w)^{1/2}/\sqrt2\)，
再用 \(b(w,w)^{1/2}\le\sqrt2\,b(u,u)^{1/2}\)。
和未加权能量界比较可得
\[
 \boxed{\quad
 \|K_N^{\rm div}F\|_{X_N^*}
 \le\sqrt{E_N}\min\{1,(1+\sqrt2)e^{-\psi_N(d)}\}
                          \|F\|_{\mathcal E^*}.
 \quad}
 \tag{93.18}
\]
该式保留真实 \(B^{-1/2}\) 的度量，不能把它无费用换成普通各分量
\(L^2\) norm。标量源与能量型源可线性相加。

## 5. 真实 regular 高角负荷到根

R74 的完整尾满足 \(\Gamma_H\ge|D_\theta|/7\) 于物理非零模。
由 (93.13) 的完整 Robin 项，
\[
 \||D_\theta|^{1/2}H_Na(L)\|_2
 \le\sqrt{14E_N}\,e^{-\psi_N(L)}\|a\|_{X_N}.
 \tag{93.19}
\]
因此实际 regular 高角 Robin 负荷 \(g\)，按物理齐次
\(H^{-1/2}\) norm，有
\[
 \boxed{\quad
 \|K_{N,\rm reg}g\|_{X_N^*}
 \le\sqrt{7E_N}
       \min\{1,\sqrt2e^{-\psi_N(L)}\}\|g\|_{H^{-1/2}}.
 \quad}
 \tag{93.20}
\]
源转换中的真实 \(J,R_m\) 等先形成这个 \(g\)，并不因本篇省去。
该非零模不等式不包括 regular 均值；\(\xi,\lambda\) 继续是
完整低系统的实际有限槽。

## 6. 当前有向常数与完整系统的限制

源 scripts/fourfold_phase_physical_high_agmon_budget.py 从同一 55 格
和 R90 已完成报告重算全部数字，核准确覆盖、参数包含、共同
origin/direction 身份。报告为
notes/2026-11-12-actual-physical-high-agmon-budget.json。
下表是向外放宽后的实际限制 contact 上界：

| 物理 \(N\) | \(L^2\) 源支撑 \(s\ge1/256\) | \(L^2\) 源支撑 \(s\ge.0116\) | regular 高角 \(H^{-1/2}\) 源 |
|---:|---:|---:|---:|
| 64 | 21.596427 | 21.596427 | 161.362857 |
| 256 | 9.777196 | 5.207255 | 121.460182 |
| 1024 | 3.828876 | .166759 | 10.059388 |
| 4096 | .240531 | \(8.734086\,10^{-7}\) | .000133267 |
| 16384 | \(1.629641\,10^{-5}\) | \(2.859310\,10^{-27}\) | \(1.099962\,10^{-24}\) |

报告另保存其他切值、各支持距离的真实作用量和 (93.18) 的弱源费。
对 \(N=4096,16384\)，到 regular 端的作用量分别大于
\(15.56817726,62.26130938\)。

以上是同一整帽、真实无限尾的物理高角限制结果，能用于完整 Schur
的高体子问题。其解仍可能有低体残差和低根通量；本篇没有把这些
cross 设零。canonical 高频 trial 仍须按 R92 的真实列和尾变到
物理分解，也没有把 R91 的窄 cutoff 直接宣称已获得本表某个远根
支持距离。完整反馈逆和非线性零解仍未由本篇授予。

重放：

    OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
    python -u scripts/fourfold_phase_physical_high_agmon_budget.py \
      --out notes/2026-11-12-actual-physical-high-agmon-budget.json
