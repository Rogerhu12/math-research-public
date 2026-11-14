# 实际半整数权 theta 的临界除 $p$ 导数

日期：2026-11-12。状态：热方程常数、临界同余、真正整的除 $p$
模形式及其 Fermat-quotient Fourier 项已证明。
尚未证明该模形式在指定 CM 点的归一值对无穷多个惰性素数为单位。

## 1. 固定的实际 theta 模形式

沿用[实际截面的 Gaussian 认证](2026-11-12-degree17-theta-gaussian-and-denominator-certificate.md)。
令 $\lambda$ 是模 $17$ 的四次特征，$\lambda(3)=-i$，并置

$$
 a_n=\begin{cases}
 \lambda(n)\exp(2\pi_{\mathbb C}i\,19n^2/289),&17\nmid n,\\
 0,&17\mid n.
 \end{cases}
$$

这些系数属于固定 cyclotomic 数域，周期为 $289$，且 $a_{-n}=a_n$。
定义

$$
 F(\tau)=\sum_{n\in\mathbb Z}a_nq^{n^2/(2\cdot17^2)},
 \qquad q=e^{2\pi_{\mathbb C}i\tau}.
 \tag{1}
$$

它是固定半整数权 $1/2$ 的 theta 模形式。
例如将 $n/17$ 按偶格 $34\mathbb Z$ 的陪集分组，就把 (1) 写成
一个固定有限 Weil 表示的标准 theta 函数的线性组合。
因此可以取一个固定的 metaplectic congruence 群；其 level 的素因子
只有 $2,17$。这里不需要猜测最小 level，也没有把它视为 level one
整数权模形式。

相应的 Hermite 生成函数是

$$
 B(t)=e^{-t^2}\sum_{n\in\mathbb Z}a_n
       e^{-\pi_{\mathbb C}(n/17)^2+2\sqrt{2\pi_{\mathbb C}}(n/17)t}
       =\sum_mB_mt^m.
 \tag{2}
$$

取本题 $E:y^2=x^3-17x$ 的周期 $\Omega_E$，并置

$$
 \alpha=4-i,\qquad
 c_{17}=\sqrt{\pi_{\mathbb C}/2}\,17/\Omega_E,\qquad
 h=c_{17}/\alpha.
$$

实际归一截面 $A(z)=\sum b_mz^m$ 满足

$$
 b_m=\frac{B_m}{B_4}h^{m-4},\qquad b_4=1.
 \tag{3}
$$

特别地 $B_0=B_2=0$，且 $B_4\ne0$。

## 2. 热方程的全部常数

记

$$
 D=\frac1{2\pi_{\mathbb C}i}\frac d{d\tau},\qquad
 \partial_k=D-\frac{k}{4\pi_{\mathbb C}\operatorname{Im}\tau}.
$$

迭代 $\partial_k$ 时，每一步把权增加 $2$。
对权 $k$ 模形式 $f$，有

$$
 \partial_k^N f
 =\sum_{j=0}^N\binom Nj(k+j)_{N-j}
     \left(-\frac1{4\pi_{\mathbb C}y}\right)^{N-j}D^jf,
 \tag{4}
$$

其中 $(a)_r=a(a+1)\cdots(a+r-1)$。
这可直接由 $D(1/(4\pi_{\mathbb C}y))=(1/(4\pi_{\mathbb C}y))^2$
归纳证明。

将 Hermite 多项式
$H_{2N}(X)=(2N)!\sum_{j=0}^N(-1)^{N-j}(2X)^{2j}/((N-j)!(2j)!)$
与 (4) 比较，或用其偶次生成函数，得到精确公式

$$
 \boxed{\quad
 B_{2N}=\frac{(16\pi_{\mathbb C})^N}{(2N)!}
                       \partial_{1/2}^NF(i).
 \quad} \tag{5}
$$

例如 $N=1$ 时，$B_2=[t^2]B(t)$ 两边逐项的多项式都是
$4\pi_{\mathbb C}(n/17)^2-1$；乘 $2!$ 才得到
$8\pi_{\mathbb C}(n/17)^2-2$。这也固定了 $16\pi$ 的规范。
结合 (3)，得

$$
 \boxed{\quad
 b_{2N}=\frac{24(16\pi_{\mathbb C}h^2)^{N-2}}{(2N)!}
            \frac{\partial_{1/2}^NF(i)}{\partial_{1/2}^2F(i)}.
 \quad} \tag{6}
$$

本题 $m=p+1$ 时，$N=(p+1)/2<p$；
$(2N)!=(p+1)!$ 恰含一个 $p$。
这个 $p$ 不能因 $N!$ 是单位而被删去。

由 $B_0=B_2=0$，另有
$F(i)=DF(i)=\partial_{1/2}F(i)=0$。

## 3. 使用真正的整高阶 Serre 导数

仅说 (4) 的非全纯项含 $p$，然后直接在 supersingular CM 点
代入一个不齐次的 Fourier 同余，并不够。
下面用整的 holomorphic modular forms 消除这一步的歧义。

记 $\vartheta_k=D-(k/12)E_2$ 为 Serre 导数，令 $k=1/2$，并定义

$$
 R_0=F,\quad R_1=\vartheta_kF,
 \quad
 R_{n+1}=\vartheta_{k+2n}R_n
            -\frac{n(k+n-1)}{144}E_4R_{n-1}\quad(n\ge1).
 \tag{7}
$$

每个 $R_n$ 都是同一固定群及 multiplier 上的 holomorphic modular
form，权为 $k+2n$。
对全部目标 $p\ge7$，它们有 $p$ 整 Fourier 系数；(7) 的固定分母
只有 $2,3$。

置 $Y=E_2^*/12$，其中 $E_2^*=E_2-3/(\pi_{\mathbb C}y)$。
由 Ramanujan 恒等式
$\partial_2Y=Y^2-E_4/144$，归纳得到

$$
 \partial_k^NF
  =\sum_{j=0}^N\binom Nj(k+N-j)_j\,Y^jR_{N-j}.
 \tag{8}
$$

将 $E_2^*$ 换成 $E_2$，同样有

$$
 D^NF
  =\sum_{j=0}^N\binom Nj(k+N-j)_j
                (E_2/12)^jR_{N-j}.
 \tag{9}
$$

这些等式也给 (7) 的逐阶验证方法：先核 $N=0,1$，
再微分；$E_4$ 项正由 $\partial_2Y$ 的第二项产生。

现在固定 $p\ge7$、$p\equiv3\pmod4$，并置

$$
 N=(p+1)/2,\qquad \epsilon_p=\left(\frac2p\right).
$$

对每个 $j\ge1$，(8)–(9) 的上升阶乘最后一项都是
$k+N-1=p/2$，且其余项没有额外的 $p$ 分母。
所以

$$
 d_{p,j}:=\frac1p\binom Nj(k+N-j)_j\in\mathbb Z_{(p)},
 \qquad
 \partial_k^NF=R_N+p\sum_{j=1}^Nd_{p,j}Y^jR_{N-j}.
 \tag{10}
$$

## 4. 临界 Katz 同余与一个真正整的除 $p$ 模形式

平方 Fourier 支撑给

$$
 D^NF\equiv\epsilon_pDF\pmod p.
 \tag{11}
$$

事实上，令 $x=n/17$，则
$(x^2/2)^N\equiv2^{1-N}(x^2/2)$，且
$2^{1-N}=2^{-(p-1)/2}\equiv\epsilon_p$。
$p\mid n$ 的项两边都为零。

取标准归一 Eisenstein series，置

$$
 \mathcal K_p=E_{p-1}\left(DF-\frac1{24}E_2F\right)
                  +\frac1{24}E_{p+1}F.
 \tag{12}
$$

这是真正的 holomorphic modular form，权为 $p+3/2$，与 $R_N$ 相同。
$E_{p-1}\equiv1$、$E_{p+1}\equiv E_2\pmod p$ 给
$\mathcal K_p\equiv DF\pmod p$。
这些基本 Eisenstein 同余可由归一系数及 Kummer 同余直接得到；
一手的明确记录见 Ahlgren–Hanson–Raum–Richter (2026) 的式 (1.1)–(1.3)，
引用列于第 7 节。

结合 (9)–(11)，两项同权的 holomorphic forms 满足

$$
 R_N\equiv\epsilon_p\mathcal K_p\pmod p.
$$

因此可定义真正的整模形式

$$
 \boxed{\quad
 V_p=\frac{R_N-\epsilon_p\mathcal K_p}{p}.
 \quad} \tag{13}
$$

这里取商的理由是同权 holomorphic forms 的 $q$-expansion principle；
不是把 $E_{p-1}$ 当成在所有 CM fiber 都等于 $1$。
全近全纯的除 $p$ 形式准确为

$$
 \frac{\partial_k^NF-\epsilon_p\mathcal K_p}{p}
      =V_p+\sum_{j=1}^Nd_{p,j}Y^jR_{N-j}.
 \tag{14}
$$

在 $\tau=i$，$E_2^*(i)=0$。
又 $p-1\equiv2\pmod4$，所以 $E_{p-1}(i)=0$ 精确成立，
而 $F(i)=0$。故 $\mathcal K_p(i)=0$，于是

$$
 \boxed{\qquad \partial_{1/2}^NF(i)/p=V_p(i).\qquad}
 \tag{15}
$$

这说明目标的下一层确实是一个明确的整模形式在固定 CM 点的值。
其 level 固定，权 $p+3/2$ 及定义中的除 $p$ 操作仍随 $p$ 变化。

## 5. 与实际 $b_{p+1}$ 的无歧义归一

不把未归一的复数 $V_p(i)$ 直接赋予 $p$ 进赋值。
定义

$$
 \mathscr V_p=
 24(16\pi_{\mathbb C}h^2)^{N-2}
          \frac{V_p(i)}{\partial_{1/2}^2F(i)}.
 \tag{16}
$$

(6)、(15) 给出准确的有理数等式

$$
 \boxed{\qquad
 \mathscr V_p=\frac{(p+1)!}{p}\,b_{p+1}\in\mathbb Q.
 \qquad} \tag{17}
$$

此前的实际截面证明已经给 $b_{p+1}\in\mathbb Z_{(p)}$。
由于 $(p+1)!/p\equiv-1\pmod p$，

$$
 v_p(\mathscr V_p)=v_p(b_{p+1}),\qquad
 b_{p+1}\equiv-\mathscr V_p\pmod p.
 \tag{18}
$$

因此新的 CM-value 判据没有未核的周期单位，也没有损失阶乘的那一层 $p$。
它尚需证明 $\mathscr V_p\ne0\pmod p$ 在无穷多个惰性素数上成立。

## 6. 除 $p$ 后确实出现了 mod $p^2$ 信息

对 $x\in\mathbb Z_{(p)}^\times$，记
$Q_p(x)=(x^{p-1}-1)/p$。置

$$
 W_p=\sum_{\substack{n\in\mathbb Z\\p\nmid n}}
           a_n(n/17)^2Q_p(n/17)q^{n^2/(2\cdot17^2)}.
 \tag{19}
$$

这是整 Fourier 级数，但不先宣称它单独就是某个固定权的模形式。
令 $u_p=2^{-(p-1)/2}$。逐 Fourier 系数计算给

$$
 \frac{D^NF-u_pDF}{p}\equiv\frac{\epsilon_p}{2}W_p\pmod p.
$$

对 $p\mid n$ 的项，$x^2$ 至少含 $p^2$，所以除 $p$ 后仍消失；
这一部分没有漏掉。
由 $u_p^2=2^{-(p-1)}$，
$(u_p-\epsilon_p)/p\equiv-\epsilon_pQ_p(2)/2\pmod p$。
所以

$$
 \boxed{\quad
 \frac{D^NF-\epsilon_pDF}{p}
      \equiv\frac{\epsilon_p}{2}
                 \bigl(W_p-Q_p(2)DF\bigr)\pmod p.
 \quad} \tag{20}
$$

为显示与真正模形式 (13) 的全部修正项，记两个整 $q$-series

$$
 A_p^{(1)}=\frac{E_{p-1}-1}{p},\qquad
 C_p^{(1)}=\frac{E_{p+1}-E_{p-1}E_2}{p}.
$$

由 (9)、(12)、(20)，完整的 Fourier 同余是

$$
 \begin{aligned}
 V_p\equiv{}&\frac{\epsilon_p}{2}
                   \bigl(W_p-Q_p(2)DF\bigr)\\
 &-\sum_{j=1}^Nd_{p,j}(E_2/12)^jR_{N-j}
 -\epsilon_p A_p^{(1)}DF
 -\frac{\epsilon_p}{24}C_p^{(1)}F\pmod p.
 \end{aligned}
 \tag{21}
$$

等式右边整体是 (13) 的模形式。
其中某个不齐次 $q$-series 不能单独在 supersingular 点取值后，
再把 Fourier 同余误当同权的几何同余。

具体地，Fermat 商没有只由模 $p$ 数据决定。
对 $x$ 为单位，有

$$
 Q_p(x+pc)-Q_p(x)\equiv-c/x\pmod p.
 \tag{22}
$$

取 $n\mapsto n+289p$ 时，固定权重 $a_n$、$n\pmod p$ 都保持不变，
但 $x=n/17$ 变为 $x+17p$，(22) 的差是 $-17/x\ne0$。
所以 (19) 真正保留了新的 mod $p^2$ 剩余；
固定的 level-$17$ theta 权重与模 $p$ Frobenius 置换本身并未指定它。
这不排除以后在 (21) 的完整修正组合中发现额外相消。

## 7. 新近 theta-cycle 结果的准确范围

一手来源如下：

- S. Ahlgren、M. Hanson、M. Raum、O. K. Richter，
  *Eisenstein series modulo $p^2$*，Forum Mathematicum **38** (2026), 93–102；
  [DOI 10.1515/forum-2024-0470](https://doi.org/10.1515/forum-2024-0470)，
  [arXiv:2502.16917](https://arxiv.org/pdf/2502.16917)。
  Theorem 1.2 与紧接的 Remark (1) 给
  $E_2E_{p-1}\equiv\partial^{\rm RS}E_{p-1}+pE_{p+1}^p\pmod{p^2}$，
  这里该文 $\partial^{\rm RS}_k=12D-kE_2$。
  这是 $q$-series 同余；在 supersingular CM 点必须继续保持同权与
  整格，不能任意除去 Hasse invariant。
- S. Ahlgren、M. Raum、O. K. Richter，
  *Theta cycles of modular forms modulo $p^2$*，Canadian Journal of Mathematics，
  2026 年 4 月 13 日 online；
  [arXiv:2604.06049](https://arxiv.org/pdf/2604.06049)。
  Theorem A 处理 $\mathrm{SL}_2(\mathbb Z)$ 上偶整数权
  $0<k<p$、且 $\omega_p(f)=k$ 的模形式，确定前一段 theta cycle 的
  全局权 filtration。

第二个定理既不直接包含 (1) 的半整数权与固定 level，也不声称某个
全局非零模形式在指定 supersingular 点的值非零。
第一个定理可用于 (21) 的 Eisenstein 修正，但尚未消去 $W_p$
及实际 CM fiber 的非零问题。

## 附录：十七点公式可只用 norm-$17$ 除法函数

[十七维 theta 基笔记](2026-11-12-inert-seventeen-theta-basis-and-divided-jet.md)
中的 $R_S=T+S$ 满足 $\bar\alpha R_S=T$。
CM sigma 除法恒等式直接给

$$
 U_S=-\frac{\delta\log\Psi_{\bar\alpha}(R_S)}{17}.
 \tag{23}
$$

这也是对全部目标素数都整的固定低次数输入。
对于 $p$ 次导数，$U_T(w)=\zeta(T+w)-\zeta(T)$ 是奇函数，
所以 $\delta^{p-1}U_T(0)=0$。
对 CM 除法恒等式求 $p-1$ 次导数，再用
$\delta^{p-1}(\delta\log\Psi_{\bar\alpha})
=-(\delta\log\Psi_{\bar\alpha})^p\pmod p$，
即得 $U_S^p=\delta^{p-2}X(R_S)$。
这给同一先导取消的较短证明，仍没有省去 (17) 或十七点公式中的
模 $p^2$ 剩余。
