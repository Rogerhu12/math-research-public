# R107：完整弱散度源的真实 Cauchy 与幅度传递

2026-11-12，visible-exact-astra-f6a2。

**状态：完整证明的弱源接线与强范数接口。**
本篇把已经保存的真实核心弱残差，直接接到 R46 的同一 Cauchy 传播和
R104 的一阶损失逆。径向散度源通过准确改变通量变量处理；不要求一个
尚未计算的径向导数，也不把它偷偷当作普通标量源。全部角频率、均值、
物理切口以及端点通量修正均保留。

没有新增几何或 ODE 数值。实际完整传播常数、相应系数乘子、连续强
残差 Gram 和最终反馈逆仍须支付。本篇不是这些常数已经通过的声明。

## 1. 同一个真实严格负型算子

取一个实际闭区间 $I=[r_-,r_+]$，$L=r_+-r_->0$，角周期为 $2\pi$。
所有函数可以限制到本题的四重子空间，但仍使用物理导数
$D_\theta=\partial_\theta$，其非零频率是 $4k$，不是 $k$。
算子为
$$
 P w=\partial_r(a w_r+bw_\theta)
       +\partial_\theta(bw_r+cw_\theta)+d w,
 \qquad a>0,\quad \mu^2=b^2-ac>0 .
 \tag{107.1}
$$
在本题固定型别 R37 算子上，准确有
$$
 d=\tau+\partial_\theta\sigma,\qquad
 \alpha=a^{-1},\quad v=b/a,\quad \gamma=\mu^2/a.
 \tag{107.2}
$$
这里 $v$ 是真实漂移，不是 R102/R104 的首相位平均 $\beta$。

沿用 R46 的完整状态空间
$$
 \mathcal P_s=H^{s+1/2}_\theta\oplus H^{s-1/2}_\theta .
 \tag{107.3}
$$
非零模和零模均使用 $\langle n\rangle=(1+n^2)^{1/2}$。
R46 §2 已从准确对称双曲系统构造同一齐次传播
$\mathcal U(r,t):\mathcal P_s\to\mathcal P_s$，并给正向、反向及
任意子区间上的有限常数
$$
 \sup_{r,t\in I}\|\mathcal U(r,t)\|_{\mathcal P_s\to\mathcal P_s}
 \le \mathfrak E_s.
 \tag{107.4}
$$
本文只在实际已支付的窗口使用这个常数；有限维生成矩阵的某个
无权 norm 不是 (107.4) 的替代品。

对实数 $u$，以 R46 的完整 Wiener 乘子上界记
$$
 M_u(h)=2^{|u|/2}\sum_{n\in\mathbb Z}
              \langle n\rangle^{|u|}|\widehat h_n|.
 \tag{107.5}
$$
它控制 $M_h:H^u\to H^u$。本题四重系数在该式中仅有 $n=4k$；
不能忽略这个尺度。定义
$$
 A_s=\sup_{r\in I}M_{s+1/2}(\alpha(r)),\qquad
 V_s=\sup_{r\in I}M_{s+1/2}(v(r)),\qquad
 C_s=(A_s^2+V_s^2)^{1/2}.
 \tag{107.6}
$$
点态 $a\ge a_*>0$ 只直接给 $\|\alpha\|_\infty\le a_*^{-1}$，
不自动给这些正阶乘子。真实全角系数及其无限尾必须参与 (107.6)。

## 2. 径向散度源的准确通量变量

设真实方程按分布意义为
$$
 P w=f_0+\partial_r f_r+\partial_\theta f_\theta.
 \tag{107.7}
$$
定义**约化通量**
$$
 \boxed{\quad \bar p=a w_r+bw_\theta-f_r.\quad}
 \tag{107.8}
$$
则 (107.7) 与以下同一个两槽状态方程准确等价：
$$
 \begin{aligned}
 w_r&=\alpha\bar p-vw_\theta+\alpha f_r,\\
 \bar p_r&=\partial_\theta(\gamma w_\theta-v\bar p)-d w
          +f_0+\partial_\theta(f_\theta-vf_r).
 \end{aligned}
 \tag{107.9}
$$

**证明。** 第一式直接来自 (107.8)。又
$$
 bw_r+cw_\theta=v(\bar p+f_r)-\gamma w_\theta.
$$
将其代入 (107.7)，$\partial_r f_r$ 与 (107.8) 中的同一项准确
抵消，剩下第二式。反向代入也得到 (107.7)，所以这不是只在
光滑试函数上得到的单向估计。对初始角导数 $q=w_\theta$，
微分第一式给
$$
 q_r=\partial_\theta(\alpha\bar p-vq)
                      +\partial_\theta(\alpha f_r),
$$
因此 R46 的三槽约束在这个实际非齐次系统中仍保持。证毕。

特别，在 $\bar p$ 方程中出现的只有
$\partial_\theta(f_\theta-vf_r)$。没有出现
$\partial_r f_r$、$\partial_r a$ 乘 $f_r$ 或另一个被省略的径向
源导数。漂移乘法 $vf_r$ 及其角向作用已完整保留。

同一弱形式也核对了真实边界符号。令
$$
 \mathfrak b(w,\psi)=\int_I\int
   (a w_r+bw_\theta)\overline{\psi_r}
  +(bw_r+cw_\theta)\overline{\psi_\theta}
  -d w\overline\psi .
$$
则准确有
$$
 \boxed{
 \mathfrak b(w,\psi)
 -[\langle\bar p,\psi\rangle]_{r_-}^{r_+}
 =\int_I\int
   f_r\overline{\psi_r}
  +f_\theta\overline{\psi_\theta}
  -f_0\overline\psi .}
 \tag{107.10}
$$
在 $f_r$ 只有体内范数而没有端点迹时，(107.10)和连续状态方程
定义的是 $\bar p$ 的弱边界通量；不能再凭空给 $f_r(r_\pm)$ 赋值。

## 3. 真实传播与强源范数

把 (107.9) 中的实际非齐次状态记为
$$
 F_{\rm st}=
 \binom{\alpha f_r}
       {f_0+\partial_\theta(f_\theta-vf_r)} .
 \tag{107.11}
$$
对每个已付实数 $s$，有
$$
 \boxed{
 \|F_{\rm st}(r)\|_{\mathcal P_s}
 \le \|f_0(r)\|_{H^{s-1/2}}
     +\|f_\theta(r)\|_{H^{s+1/2}}
     +C_s\|f_r(r)\|_{H^{s+1/2}}.}
 \tag{107.12}
$$
事实上 $\|\partial_\theta h\|_{H^{s-1/2}}\le
\|h\|_{H^{s+1/2}}$，而 $f_r$ 的两槽贡献分别由 $A_s,V_s$ 控制；
在两槽 Hilbert 直和中合并它们给 $C_s$。其余两项使用三角不等式。

Duhamel 式是
$$
 \boxed{
 \binom{w}{\bar p}(r)
 =\mathcal U(r,t)\binom{w}{\bar p}(t)
       +\int_t^r\mathcal U(r,z)F_{\rm st}(z)\,dz .}
 \tag{107.13}
$$
它使用原算子的齐次传播，因为齐次时 $\bar p$ 就是真实物理 conormal。
当 $r<t$ 时，积分具有通常的有向符号，估计使用无向区间。
由 (107.4)、(107.12) 得
$$
 \left\|\binom{w}{\bar p}(r)\right\|_{\mathcal P_s}
 \le \mathfrak E_s\left[
 \left\|\binom{w}{\bar p}(t)\right\|_{\mathcal P_s}
 +\int_{[r,t]}\!
  \left(\|f_0\|_{H^{s-1/2}}+\|f_\theta\|_{H^{s+1/2}}
                         +C_s\|f_r\|_{H^{s+1/2}}\right)dz
                      \right].
 \tag{107.14}
$$
由 $L^2$ 体源转换时，准确使用
$$
 \int_I\|h(r)\|\,dr\le\sqrt L\,\|h\|_{L^2(I)}.
 \tag{107.15}
$$
这是同一真实长度，不是每个小 span 都额外支付一次全长。

对于足够光滑源，(107.13)直接由微分验证。一般源满足
$f_0\in L^1H^{s-1/2}$、
$f_r,f_\theta\in L^1H^{s+1/2}$ 时，(107.11)属于
$L^1(I;\mathcal P_s)$，因而由 Bochner 积分定义连续状态。
光滑逼近、(107.14)及分布恒等式给一般的存在、唯一性与 (107.10)。
真实系数在径向分段光滑时，逐段使用同一式并匹配连续的 $(w,\bar p)$；
不要求 $f_r$ 或切向通量跨片具有相同径向导数。

## 4. 实际连续有限参考的三个残差正好适用

使用已保存的连续有限参考 $(w_N,p_N)$。
这里 $p_N$ 已恢复到**物理**通量，不能仍使用保存状态的 $p_N/8$。
固定四重保留投影 $P_N$，$P_H=I-P_N$，定义原来已经证明的完整残差
$$
 \begin{aligned}
 R_r&=a(w_N)_r+b(w_N)_\theta-p_N,\\
 R_\theta&=P_H\bigl(b(w_N)_r+c(w_N)_\theta+\sigma w_N\bigr),\\
 R_0&=\sigma(w_N)_\theta-\tau w_N-(p_N)_r
   -\partial_\theta P_N
      \bigl(b(w_N)_r+c(w_N)_\theta+\sigma w_N\bigr).
 \end{aligned}
 \tag{107.16}
$$
全部有限输出缺陷仍在 $R_r,R_0$ 中；不能只保它们的高模。

**准确的强/分布身份为**
$$
 \boxed{\quad
 P w_N=\partial_rR_r+\partial_\theta R_\theta-R_0.
 \quad}
 \tag{107.17}
$$

**证明。** 置
$z=b(w_N)_r+c(w_N)_\theta+\sigma w_N$。
由 (107.16)，
$$
 R_0=\sigma(w_N)_\theta-\tau w_N-(p_N)_r
                              -\partial_\theta P_Nz.
$$
于是
$$
 \begin{aligned}
 \partial_rR_r+\partial_\theta R_\theta-R_0
 &=\partial_r(a(w_N)_r+b(w_N)_\theta)
    +\partial_\theta z
    -\sigma(w_N)_\theta+\tau w_N\\
 &=\partial_r(a(w_N)_r+b(w_N)_\theta)
    +\partial_\theta(b(w_N)_r+c(w_N)_\theta)
    +(\tau+\sigma_\theta)w_N=P w_N .
 \end{aligned}
$$
由于 $p_N$ 在所有拼接点准确连续，分布微分没有隐藏的有限通量
delta 项；物理通量的可能跳跃全部由 $R_r$ 的散度表示。证毕。

因此这里应准确使用
$$
 f_r=R_r,\qquad f_\theta=R_\theta,\qquad f_0=-R_0,\qquad
 \bar p=p_N.
 \tag{107.18}
$$
这说明已有弱残差 Gram 的三种源可以直接代入 (107.12)。
不用先对 $R_r$ 求径向导数，也不用在高标量源中添加不存在的
$\partial_\theta P_Nz$：
$$
 P_HR_0=P_H\bigl(\sigma(w_N)_\theta-\tau w_N\bigr)
$$
仍是原来的准确恒等式。

若 $u$ 是同一个真算子的齐次解，令 $e=w_N-u$，
则误差状态的约化通量为
$$
 \bar p_e=p_N-p_u .
 \tag{107.19}
$$
故 (107.14)直接控制“有限参考通量 $p_N$ 与真通量”的差。
这不假设整个无限核心 Dirichlet 问题可逆；若初始误差未知，仍要
由原来的两通道/完整全局反馈确定它。

## 5. 接入准确幅度 frame，保留所有切口修正

令 $\mathscr F(r):E_s\to\mathcal P_s$ 为 R46 (3.1) 的完整通量 frame，
其中包括实际 height、normal shear、两个幅度支和均值。记其真逆界
$$
 \|\mathscr F(r)^{-1}:\mathcal P_s\to E_s\|\le I_s(r).
$$
对于约化状态，完整体源幅度为
$$
 \boxed{
 z_{\rm body}(r)=
 \mathscr F(r)^{-1}\int_t^r\mathcal U(r,z)
 \binom{\alpha f_r}
       {f_0+\partial_\theta(f_\theta-vf_r)}(z)\,dz .}
 \tag{107.20}
$$
其 norm 不超过 (107.14) 中的体源项乘 $I_s(r)$。
该式保留非齐次源的符号与两个 Cauchy 槽；不能只把下面一槽叫作
R46 (6.12) 的原普通源。

如果物理接线需要真实 conormal $p$ 而不是约化通量，并且
$f_r(r)$ 的对应端点迹已经支付，必须同时加
$$
 \boxed{\quad
 z_{\rm phys}(r)=
   \mathscr F(r)^{-1}\binom{w}{\bar p}(r)
       +\mathscr F(r)^{-1}\binom{0}{f_r(r)}.
 \quad}
 \tag{107.21}
$$
从物理初值开始时也须先减去 $f_r(t)$。
端点贡献在 $E_s$ 中的界为
$I_s(r)\|f_r(r)\|_{H^{s-1/2}}$。
只有体内 $L^2$ 范数不给端点迹，不能据此免费把 (107.21) 的最后
一项设为零。若比较的是 (107.19)，需要的输出本来就是约化通量
误差；此时不能重复再加同一份 $R_r$。

多段拼接有两种等价的准确做法：使用真实物理通量并逐接口保留
(107.21)，或在每段使用约化通量并保留其由 $f_r$ 跳跃引起的准确
转换。若真实问题有额外给定的界面 delta 源，其独立通量跳跃另加，
不由一个体内 Gram 自动覆盖。

## 6. R104 的一阶损失需要哪些实际源档

R104 的真高逆要求幅度右端属于其已经归一化的 $E_{s+1}$，才能给解的 $E_s$。
因此在 (107.20) 中必须用 $s+1$ 的 Cauchy 窗口。
还须保留从本篇物理切口幅度到 R104 实际返回 frame 的真实源接线
$\mathcal W_{s+1}$，并支付
$
 \|\mathcal W_{s+1}:E_{s+1}^{\rm cut}\to E_{s+1}^{\rm R104}\|
 \le K_{s+1}^{\rm wire}.
 \tag{107.21a}
$
它包括物理频率 $4k$ 到标签频率 $k$ 的规范、完整角共轭
$\mathscr G_H$ 和实际端口操作。局部源界不自动给这些操作 norm 为1。
若接线有额外导数损失，必须相应提高源档；以下 corollary 的前提是
(107.21a) 在写出的同一档已经证明。
最基本的 $s=0$ 档，实际需要
$$
 f_0\in L^2(I;H^{1/2}),\qquad
 f_r,f_\theta\in L^2(I;H^{3/2}),
 \tag{107.22}
$$
而不是把一个 $H^{-1/2}$ 通量费改名成强源。
在同一真实对象上，若完整三源算子满足
$$
 \|R_0:X\to L^2H^{1/2}\|\le r_0,\quad
 \|R_\theta:X\to L^2H^{3/2}\|\le r_\theta,\quad
 \|R_r:X\to L^2H^{3/2}\|\le r_r ,
$$
则
$$
 \boxed{
 \|z_{\rm body}:X\to E_1\|
 \le I_1(r)\mathfrak E_1\sqrt L\,
           (r_0+r_\theta+C_1r_r).}
 \tag{107.23}
$$
将 (107.23) 注入 R104 前还须乘 $K_1^{\rm wire}$；
随后 R104 的准确 $\mathcal T^{-1}$ 源变换至多再乘 $2$。
在其实际高块收缩门通过后，归一化高逆界为 $220/7$；
所以这条完整体源的高解费至多为
$$
 \frac{440}{7}\,K_1^{\rm wire}I_1(r)\mathfrak E_1\sqrt L\,
           (r_0+r_\theta+C_1r_r).
 \tag{107.24}
$$
这是在其它真实端口和有限 Schur 已按 R104 保留的归一坐标中的
一个源分项，不是整个 PDE 右逆的最终常数。
解回到 $\mathcal T$ 前坐标时还应乘其 $3/2$ 重建费；
物理重建另用相应实际 frame。
两个反馈端的源向量应在同一全直和范数中合并，不能免费取每项最大值。

已保存的
[完整核心强弱残差接口](../notes/2026-11-12-core-strong-weak-residual-contract.md)
明确计算 $H^0,H^{1/2},H^1,H^{3/2}$ 的全 Fourier Gram、无限补集、
连续参考及有限缺陷。其 $H^{1/2}$ 标量行和 $H^{3/2}$ 两条弱通量行
正好供应 (107.22)。这些新 Gram 在执行器失联前尚未实际计算；
本文只是证明应使用的强档与真实源转换恰好匹配。

## 7. 输入矩阵 Gram、均值及对称子空间

上述结论同样适用于从任意有限或 Hilbert 输入空间 $X$ 到实际源的
线性算子。设已经证明完整 PSD 上界 $G_0,G_\theta,G_r$：
$$
 R_0^*R_0\preceq G_0,\qquad
 R_\theta^*R_\theta\preceq G_\theta,\qquad
 R_r^*R_r\preceq G_r
$$
分别在 (107.22) 的体源空间中取伴随。任取正数
$\lambda_0,\lambda_\theta,\lambda_r$，则加权 Cauchy--Schwarz 给
$$
 \begin{aligned}
 \left(r_0(x)+r_\theta(x)+C_1r_r(x)\right)^2
 \le{}&(\lambda_0+\lambda_\theta+\lambda_r)\\
 &\cdot\left\langle
 \left(\frac{G_0}{\lambda_0}
       +\frac{G_\theta}{\lambda_\theta}
       +\frac{C_1^2G_r}{\lambda_r}\right)x,x\right\rangle ,
 \end{aligned}
 \tag{107.25}
$$
其中 $r_j(x)$ 是对应真源范数。乘上
$I_1(r)^2\mathfrak E_1^2L$ 即为 (107.23) 的算子 Gram 上界。
也可直接保留 (107.11) 的全部交叉项，计算更紧的联合 Gram。
这两种做法均保留整个输入列空间；逐列上界不能不付输入聚合费就
当成完整算子 norm。

零模一直在这些空间内。$\partial_\theta$ 杀去某个单项的角平均，
不意味着 $\bar p_0$、$f_{0,0}$、$(\alpha f_r)_0$ 或真实 regular
端口为零。它们仍按 (107.9)、(107.20)及完整 Schur 接线传播。

当准确 R71 群作用与真实算子和输入约束交换时，可在所选不变子空间
应用同一个证明及原来的 norm 上界。这不会删除 retained mean、
regular 行或所需的物理 source。R105 的六维低扇区是有限入口；
(107.20)的体源仍具有全部实际无限角输出。

## 8. 数值与应用边界

本篇全部等式由真实算子、分布分部积分、R46 已证明的传播和
Hilbert 范数不等式推出；没有把有限矩阵试验作为证明。

实际应用还须在同一个最终参数和同一邻域支付：

- R46 的完整 $\mathfrak E_1$、局部 frame $I_1$ 及到 R104 的真实源接线 $K_1^{\rm wire}$；
- $a^{-1}$、$b/a$ 的实际 $M_{3/2}$，含全部 Fourier 尾及参数变化；
- 三个连续完整体源的相应强 Gram；
- 需要物理 flux 接口时的真实径向弱源端点迹；
- R104 的完整强余项/有效高切以及有限低高 Schur。

这些值不能从已有 $175$ 个局部转移误差之和推出，也不能由点态
正性或某个中心 Fourier 矩阵无偿升级。
已付的新内容是准确源变量、完整边界符号、避免径向求导的真实
Cauchy 公式，以及与当前强 Gram 档和一阶损失逆的明确接合。
固定开握持区的非线性迭代与同一族的几何预算仍继续。

