# R131：全部正物理段长上的显式正径向参数与完整 JVP

2026-11-12，constructive_geometry。本文只替换 `CoastDesignProfile` 的计算径向坐标，不改任何固定 $T$ 下的物理度量。$T$ 本身仍是改变物理前缀的外层设计参数；选定解后，必须冻结该 $T$ 才能进行同一个 $g$ 的加密。

## 1. 问题及完整结论

既有 `PartialReturnParameter` 的两个可变直行段分别满足

\[
L_m(T)=T,\qquad
L_d(T)=L_d(T_0)+d(T-T_0),\qquad
d=-v_m/v_d<0.
\tag{1}
\]

这里 $v_m,v_d<0$ 是这两段的固定径向速度，且所有其他段的长度固定。物理正长度条件恰为

\[
0<T<T_{\max}:=T_0-L_d(T_0)/d.
\tag{2}
\]

旧五次坐标插值另外要求某个导数下界为正；它可以在 (2) 内失效。下面给出一个新的、联合光滑的计算坐标：对 **每个** 满足 (2) 的 $T$ 都严格单调，接口处保留 $s_x=1,s_{xx}=0$，因而与其他段的平移拼成整个径向区间上的 $C^2$ 微分同胚。新坐标的参数导数及逆式均有显式公式，不需要求数值逆矩，也不除以尾部的 $b$ 或 $n$。

## 2. 一个任意正长度比的准确映射

固定参考段长 $L_*>0$，实际段长 $L>0$，记

\[
q=L/L_*,\quad \tau\in[0,1],\quad
t=\pi\tau,\quad C=\cos t,\quad S=\sin t,
\quad D=q^2C^2+S^2>0.
\tag{3}
\]

令

\[
\Theta_q(\tau)=\operatorname{Arg}(q\cos(\pi\tau)+i\sin(\pi\tau))
\in[0,\pi],
\quad
\Phi_q(\tau)=\frac{q}{\pi}\Theta_q(\tau).
\tag{4}
\]

在 $0<\tau<1$，虚部严格为正，因此这个角支无跳跃；在两端分别连续取 $0,\pi$。对每个 $q>0$，复数从不为零。局部可选实光滑角支，故 (4) 对 $\tau,q$ 联合光滑，包括从材料区间一侧取的端点导数。

直接微分给

\[
\Theta_{q,\tau}=\frac{\pi q}{D},\qquad
\boxed{\Phi_{q,\tau}=\frac{q^2}{D}>0.}
\tag{5}
\]

并且

\[
\Phi_q(0)=0,\quad \Phi_q(1)=q,\quad
\Phi_{q,\tau}(0)=\Phi_{q,\tau}(1)=1,\quad
\Phi_{q,\tau\tau}(0)=\Phi_{q,\tau\tau}(1)=0.
\tag{6}
\]

最后一式来自 $D_\tau=2\pi(1-q^2)SC$。特别地，实际正导数范围为

\[
\min(1,q^2)\le\Phi_{q,\tau}\le\max(1,q^2).
\tag{7}
\]

因此没有除正段长以外的坐标可行性限制；不要求这个下界在接近物理零段长时仍一致大于零。

## 3. 全径向拼接、逆式和度量含义

在参考坐标中的该段为 $[x_i,x_i+L_*]$，令 $\tau=(x-x_i)/L_*$，实际物理段起点为 $s_i(T)$。定义

\[
s(x,T)=s_i(T)+L_*\Phi_{q(T)}(\tau),
\qquad q(T)=L(T)/L_*.
\tag{8}
\]

端点分别为 $s_i(T)$ 与 $s_i(T)+L(T)$；又由 (5)–(6)，

\[
s_x=\frac{q^2}{D}>0,\qquad s_x|_{\partial}=1,
\qquad s_{xx}|_{\partial}=0.
\tag{9}
\]

其他固定长度段使用平移 $s=s_i(T)+x-x_i$。各段的实际端点本来连续相接，所以 (6) 使整个拼接为 $C^2$。它严格递增，连续覆盖全部实际径向区间，因而是全局微分同胚，而不只是每段内部局部可逆。

对于每个固定 $T$，若物理度量为

\[
g_T=ds^2+a(s,T)^2du^2,
\]

其计算坐标表达准确是

\[
s_x(x,T)^2dx^2+a(s(x,T),T)^2du^2.
\tag{10}
\]

因此这次更换坐标不改变物理 $g_T$。reader 的 `a_s,a_ss,c,K` 仍是物理 $s$ 导数及其形成的标量；计算径向方程应继续乘 `radial_scale=s_x`。不得把 `a_s` 误当作 $a_x$；确切有

\[
a_x=a_s s_x,\qquad a_{xx}=a_{ss}s_x^2+a_s s_{xx}.
\tag{11}
\]

新映射自己的逆也显式。给定实际归一位置 $\zeta=(s-s_i(T))/L(T)\in[0,1]$，

\[
\boxed{\tau=
\frac1\pi\operatorname{Arg}(\cos(\pi\zeta)+i q\sin(\pi\zeta)),}
\tag{12}
\]

角仍取 $[0,\pi]$。由 $\tan\Theta=\tan(\pi\tau)/q$ 及角所在半平面，(12) 恰是全区间逆，而非只在一个象限有效的 arctan 公式。

若从一个旧计算坐标的已存实际解续算，应先以真实 $s$ 对应重采样字段。两坐标在参考参数 $q=1$ 时都等于恒等映射；离开参考参数后，同一计算节点上的旧数组不自动代表同一个物理点。直接拿该数组作新初猜是允许的，但不能把这种初猜误写成同一旧实体的准确重参数化。

## 4. 完整参数导数

对 (4) 按 $q$ 微分，得到

\[
\partial_q\Theta_q=-\frac{SC}{D},\qquad
\Psi_q(\tau):=\partial_q\Phi_q(\tau)
=\frac{\Theta_q(\tau)}\pi-\frac{qSC}{\pi D}.
\tag{13}
\]

其两端值为 $\Psi_q(0)=0,\Psi_q(1)=1$。正尺度的参数导数为

\[
\partial_q\left(\frac{q^2}{D}\right)
=\frac{2qS^2}{D^2}.
\tag{14}
\]

令 $L_T=dL/dT$，则 $q_T=L_T/L_*$。在固定计算 $x$ 处，完整 JVP 为

\[
\boxed{s_T=s_{i,T}+L_T\Psi_q(\tau),\qquad
(s_x)_T=\frac{2qS^2}{D^2}\frac{L_T}{L_*}.}
\tag{15}
\]

接口处 (15) 的尺度导数为零，位置导数正好变成邻接两段的实际起点导数，因此参数微分也与全域拼接一致。

在当前物理族中，浅直行段的 $a_s=v_m$，深直行段的 $a_s=v_d$。浅段起点半径不随 $T$ 变，深段起点半径的 $T$ 导数为 $v_m$。因此将 `local_s_T` 记作 $L_T\Psi_q$，准确有

\[
a_T=
\begin{cases}
v_m\,\mathrm{local\_s}_T,&\text{浅直行段},\\
v_m+v_d\,\mathrm{local\_s}_T,&\text{深直行段},\\
v_m,&\text{浅段后、深段前的固定形状段},\\
0,&\text{其余段}.
\end{cases}
\tag{16}
\]

这里的 $a_T$ 是复合函数 $a(s(x,T),T)$ 在固定计算 $x$ 下的导数。其他段的形状仅平移，两个直行段的速度本来为常数；因而 reader 输出的物理导数字段满足

\[
(a_s)_T=(a_{ss})_T=0.
\tag{17}
\]

由 $c=a_s/a$、$K=-a_{ss}/a$，进一步得到

\[
c_T=-c\,a_T/a,\qquad K_T=-K\,a_T/a.
\tag{18}
\]

(15)–(18) 是全部现有 coast 接口所需的参数 JVP。它们不涉及 tail 的参考曲率，也在 flat cut 的 $a_s=-1,a_{ss}=0$ 处正常。

## 5. 真实实现与本次已执行检查

独立实现为
`scripts/fd2d_gc_design_profile_positive.py`，SHA-256
`bcdb757d83e4b11ba5dcb5b2489c53005e338a664aea680c0aa7623b86515a47`。
可从该模块导入 `PositiveCoastDesignProfile` 或兼容别名 `CoastDesignProfile`；旧 reader 和已绑定旧报告的源均未改变。

本次输入为
`notes/2026-11-12-fd2d-flat-cut-prefix-v1-coast-compatible-candidate.json`，SHA-256
`a92b552f70bcc26c97f16261fbc78fac10c1daad6d72eafc8063dcb093cdd147`。
其物理 $T_0=.02$、$T_{\max}\simeq.22510364412376974$。

实际执行 `fd2d_gc_design_profile_positive_check.py`，session 84434，返回 chunk 7415ff，真实 exit 0。保存的报告为
`notes/2026-11-12-fd2d-flat-cut-positive-clock-check-01.json`，SHA-256
`638e7401b07d02bcac37535dad07cd714233df75da9d02088a38c74e11108eef`。
713 个计算点以及 $T=.001,.02,.129,.15,.20,.22$ 都实际求值完成；其中旧坐标在 $.001,.15,.20,.22$ 拒绝，新坐标的采样最小尺度分别为 $.0025,.13408348,.01498052,.000619176$，与 (7) 一致。

与同一个实际物理候选在返回的 $s$ 处复合比较，$a$ 差不超过 $2.23\cdot10^{-16}$，$a_s,a_{ss}$ 差为零；全部 cut 两 jet 仍为 $(.8,-1,0)$。固定计算节点的中心差分核对完整参数导数：普通参数点的最大缩放差小于 $1.73\cdot10^{-9}$，最短浅段 $T=.001$ 为 $2.49\cdot10^{-8}$。这些是实际有限浮点核对，完整恒等式由 §§2–4 的证明给出，不把差分数字说成连续曲面证书。

物理零段长 $T=0$ 或 $T=T_{\max}$ 不属于 (2)，需要重新划分材料区间。极端正段长下的浮点上溢或下溢也应照实报为数值表示问题；它不产生任何新的精确物理参数限制。本结果解除的是坐标障碍，没有预付非圆前缀方程、接尾或强几何指标。
