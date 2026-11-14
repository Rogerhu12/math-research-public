# 两条原中央行的共同 amplitude 与完整周期 Frobenius

日期：2026-11-12。**状态：以下系数、两行联立与真正倍乘恒等式已证明。**
仍采用原平面 $(A_2,B)$。本文没有把两条中央行的零性传递给全部
混合列，也没有删去倍乘式中的正 theta 次数。

## 1. 同一个固定第一类周期

沿用 R162 的
$$
 u=x^{-1/2},\quad s=u^4,\quad v=\sqrt{1-s},\quad
 u'=v,\quad A_2=P(s)e^{W(s)},\quad B=Q(s)e^{W(s)}.
\tag{1}
$$
$P,Q$ 是该文的完整次数十六多项式，均以 $s$ 为首项。
记 $p_0=P/s$、$Z=p_0e^W$、$V=Q/P-1$；因此
$A_2=sZ$、$B=s(1+V)Z$，且 $V=-22s+\cdots$。

以原点积分规范定义
$$
 \mathcal L(s)=\frac{z(u)}u
 =\sum_{m\ge0}\frac{\binom{2m}{m}}{4^m(4m+1)}s^m,
 \qquad z(u)=\int_0^u\frac{dt}{\sqrt{1-t^4}}.
\tag{2}
$$
于是准确有
$$
 w=z^4=s\mathcal L(s)^4,\qquad
 \mathcal L+4s\mathcal L'=(1-s)^{-1/2}.
\tag{3}
$$
这里 $\mathcal L(0)=1$，所以 (3) 的两参数都使用原首系数一的
平凡化。本文不把 $\mathcal L$ 替换成一个未说明的周期单位。

对任意 $C(s)\in s\mathbb Q[[s]]$，令
$b_{4n}(C)=[z^{4n}]C(s(z))e^{W(s(z))}$。逐项换元留数给全特征零式
$$
 \boxed{\quad
 b_{4n}(C)=[s^n]\frac{C(s)e^{W(s)}}
                         {\sqrt{1-s}\,\mathcal L(s)^{4n+1}}
 \quad(n\ge1).
 \quad}\tag{4}
$$
确实，$dw/w=(s^{-1}+4\mathcal L'/\mathcal L)ds$，故
$$
 \begin{aligned}
 [w^n]C(s)e^W
 &=\operatorname{Res}_{s=0}
   \frac{C(s)e^W}{s^{n+1}\mathcal L^{4n}}
            \left(1+\frac{4s\mathcal L'}{\mathcal L}\right)ds\\
 &=[s^n]\frac{C(s)e^W}{\sqrt{1-s}\,\mathcal L^{4n+1}}.
 \end{aligned}
$$
同一式子对原任意列 $A_2^jV^c$ 也成立：将 $Ce^W$ 换成
$P^jV^ce^{jW}$。因此源格没有被扩大为任意的 $V^cA_2$。

## 2. 惰性首中央行确实只用低 amplitude

令 $p=4r-1\ge7$。在次数小于 $r$ 的范围，
$W$、$Z$、$\mathcal L^{\pm1}$ 及 $(1-s)^{-1/2}$ 都 $p$ 整。
对 $W$ 这是 R160 的准确首分母；对 $\mathcal L$，在所需范围
$4m+1$ 不能被 $p$ 除。指数的所有相关阶乘亦小于 $p$。

置固定级数
$$
 \mathcal E(s)=\frac{e^{W(s)}}{\sqrt{1-s}\,\mathcal L(s)^2},
 \qquad
 \mathcal T(s)=p_0(s)\mathcal E(s)
             =\frac{Z(s)}{\sqrt{1-s}\,\mathcal L(s)^2}.
\tag{5}
$$
它们在 $s^{r-1}$ 以前均整，且 $\mathcal T(0)=1$。
在 (4) 取 $n=r$，有 $4r+1=p+2$。
因为在这里实际只需到次数 $r-1<p$，Freshman's dream 给
$\mathcal L^{-p}\equiv1\pmod{p,s^r}$。于是
$$
 \boxed{\quad
 \begin{aligned}
 b_{p+1}(A_2)&\equiv[s^r]P\mathcal E
                         =[s^{r-1}]\mathcal T,\\
 b_{p+1}(B)&\equiv[s^r]Q\mathcal E
                         =[s^{r-1}](1+V)\mathcal T
 \end{aligned}
 \pmod p.
 \quad}\tag{6}
$$
本式没有约化 $\mathcal E$ 的首个非整系数：$P,Q$ 的一阶零
使它完全不进入 (6)。这也是先保留原分子再约化的必要原因。

写 $\mathcal T=\sum t_ms^m$、$V=\sum_{j\ge1}v_js^j$。
两条原中央首层同时为零，准确等价于
$$
 \boxed{\qquad
 t_{r-1}=0,\qquad
 \sum_{j=1}^{r-1}v_jt_{r-1-j}=0\quad\text{于 }\mathbb F_p.
 \qquad}\tag{7}
$$
对 $p\ne11$，$v_1=-22$ 是单位。这两行在长度 $r$ 的低系数
向量上独立：第一行的最高位置是 $t_{r-1}$，第二行的最高位置
是 $t_{r-2}$，其系数为 $-22$。所以第二条原中央条件确实
对第一条之外的低 amplitude 施加了约束。它没有自动控制
$[s^{r-1}]V^j\mathcal T$ 的 $j\ge2$ 各行。

例如 $p=7,r=2$ 时，第二式只剩 $v_1t_0=-22\ne0$；
故两条首层不可能同时为零。作为规范核对，准确系数给
$$
 \begin{array}{c|ccc}
 p&7&11&19\\\hline
 b_{p+1}(A_2)\bmod p&3&10&10\\
 b_{p+1}(B)\bmod p&2&10&10
 \end{array}
$$
其中第一行亦由 R51/R53 的原 $A_1$ 系数及
$A_2=A_1(2z)/16$ 独立核定。这些数值不是跨素数证明。

## 3. 第一类周期与 R166 的同一真正 Frobenius 提升

保留 R166 的整除法多项式 $D_p,H_p$，置
$$
 \rho_p=D_p/H_p,\qquad \Phi_p=s\rho_p^4.
\tag{8}
$$
该文已证明 $u(pz)=\rho_p(s)u(z)$、
$\vartheta(pz)=H_p(s)\vartheta(z)^{p^2}$，以及
$H_p\equiv1$、$D_p\equiv-s^{(p^2-1)/4}\pmod p$。
因此 (2) 的周期满足完整特征零恒等式
$$
 \boxed{\qquad
 D_p(s)\mathcal L(\Phi_p(s))
                  =pH_p(s)\mathcal L(s).
 \qquad}\tag{9}
$$
这是 $p z=u(pz)\mathcal L(s(pz))$，没有另选一个形式群同构。
将其或原不变微分微分，得到
$$
 \Phi_p'(s)=p\rho_p(s)^3
              \frac{\sqrt{1-\Phi_p(s)}}{\sqrt{1-s}}.
\tag{10}
$$
特别 $\mathcal J_p=\Phi_p'/p\in\mathbb Z_p[[s]]$。
令 $R=(p^2-1)/4$，其全级数约化准确为
$$
 \mathcal J_p\equiv-s^{3R}(1-s)^{2R}\pmod p.
\tag{11}
$$
证明使用 $\Phi_p\equiv s^{p^2}$，所以
$\sqrt{1-\Phi_p}/\sqrt{1-s}\equiv(1-s)^{(p^2-1)/2}$。
这个指数是整数，常数一的形式平方根唯一。

结合 theta 倍乘与 (9)–(10)，(5) 的实际 amplitude 精确满足
$$
 \boxed{\quad
 \mathcal E(\Phi_p)\Phi_p'
   =\frac{D_p^5H_p^{63}}p\,
         e^{(p^2-1)W}\mathcal E.
 \quad}\tag{12}
$$
若用整行 $\mathcal J_p=\Phi_p'/p$，右侧分母是 $p^2$，
不是 $p$。它们都不能省略。
对 R166 的真实连接单位
$$
 \mathscr U_p=\frac{p_0(\Phi_p)H_p^{68}}{p_0^{p^2}}
             =\frac{Z(\Phi_p)}{Z^{p^2}}\in1+ps\mathbb Z_p[[s]],
$$
等价的归一式为
$$
 \mathcal T(\Phi_p)\Phi_p'
   =\frac{\rho_p^5}{p}\mathscr U_p Z^{p^2-1}\mathcal T.
\tag{13}
$$
式 (12)–(13) 保留了真实第一类周期的权与整个正 theta 因子。
它们没有在固定两维分子空间中构造一个闭合的线性 Frobenius
矩阵；右侧仍包含 $e^{(p^2-1)W}$ 或 $Z^{p^2-1}$。

因此当前可继续使用的联合输入正是 (7) 的两条实际低行、
R166 的全部精度连接与 (9) 的完整周期式。把它们转为 R159
要求的原全部混合列、同一饱和前缀上的严格成本，仍需另证。

## 来源

- 固定 $P,Q,W$ 及原源格：R162，
  [完整非线性方程与逆参数 jet](2026-11-12-actual-theta-plane-nonlinear-flow-and-lagrange-jets.md)。
- 首分母与全部列谱：R160，
  [惰性首进位与共同次数谱](2026-11-12-inert-theta-carry-and-common-degree-spectrum.md)。
- 整 theta 除法多项式及真正 $\Phi_p$：R166，
  [原 theta 除法与全部精度连接](2026-11-12-actual-theta-division-frobenius-and-full-ghosts.md)。
- 旧 $A_1$ 的独立首层算法：
  [实际惰性对角与 Romik 接口](2026-11-12-inert-theta-romik-interface.md)。
