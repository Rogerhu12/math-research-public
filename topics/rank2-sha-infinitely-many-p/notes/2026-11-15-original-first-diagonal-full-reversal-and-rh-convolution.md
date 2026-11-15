# 原四首行的完整倒序核与第一个全低卷积闭式

日期：2026-11-15。**状态：本篇显示的有限反射、伴随式及调和和恒等式已证明。**

这是 R828 及其完整 $d$-参考运输 note 的补充。
它把原 $\log\Theta$ 的**全部首共振前系数**倒序，而不只读取四个高轴。
其中与原 $H$ 的一次完整卷积有闭式 $3r_Nq_p(3)/8$。
四条原来源所带的 $\Theta^{17},\Theta^{36},\Theta^{68},\Theta^{33}$
仍在：本篇没有用这个一次卷积替换四条首中央行，
没有证明这些行不能同时为零，也没有新增一个中央零条件。

## 1. 同一个原参数及全部单位分母

保持原惰性素数
$$
p=6s-1>211,\qquad N=s-1.
\tag{1}
$$
沿用 R821、R828 的固定坏集，不改变任何射线或原来源。
先用共同 $b=1$ 模型，取
$$
t=-x^{-3},\qquad w=z^6,\qquad
C(t)=(1-t)^{-1/2}=\sum_{j\ge0}c_jt^j,\qquad
c_j=\frac{\binom{2j}{j}}{4^j},
$$
$$
H(t)=\sum_{j\ge0}\frac{c_j}{6j+1}t^j,\qquad
z=uH(t),\quad t=-u^6,\quad w=-tH(t)^6.
\tag{2}
$$
因此这是原负角 $t$，不是 R595 中正角 $b/x^3$ 的不变号抄写。
令
$$
r_j=\frac{(1/3)_j}{(5/6)_j},\qquad
R(t)=\sum_{j\ge0}r_jt^j,\qquad
R_N(t)=\sum_{j=0}^N r_jt^j.
\tag{3}
$$
原闭式正是
$$
t\frac{d}{dt}\log\Theta=\frac{R-1}{3},\qquad
t\frac{d}{dt}\log\Theta^{17}=\frac{17}{3}(R-1).
\tag{4}
$$
对 $0\le j\le N$，本篇用到的 $r_j,c_j$、
$j!$、$(3/2)_j$、$2j+1$、$6j+1$ 均为 $p$-单位。
例如最后两个分母分别不超过 $2s-1$ 与 $p-4$；
$(5/6)_j$ 的首个 $p$-分母在 $j=s$，不在 (3) 中。
特别 $r_N\ne0\pmod p$。
以下同余都在原系数环约化后理解。

## 2. 整个低核的准确反射

对每一个 $0\le j\le N$，有
$$
\boxed{
r_{N-j}=r_N\frac{j!}{(3/2)_j}\pmod p.
}
\tag{5}
$$
事实上
$$
\frac{r_{N-j}}{r_N}
=\frac{(5/6+N-j)_j}{(1/3+N-j)_j}.
$$
由 $s\equiv1/6\pmod p$，分子、分母分别变为
$(-j)_j$ 与 $(-j-1/2)_j$；两个符号抵消即得 (5)。
这是全部 $N+1$ 个系数的等式，包含两端。

置
$$
b_j=\frac{j!}{(3/2)_j}
=\frac{4^j(j!)^2}{(2j+1)!}
=\frac1{(2j+1)c_j},
\qquad B_N(t)=\sum_{j=0}^N b_jt^j.
$$
于是
$$
\boxed{t^N R_N(t^{-1})=r_NB_N(t)\pmod p.}
\tag{6}
$$
其特征零形式母函数可以准确写为
$$
\sum_{j\ge0}b_jt^j
={}_2F_1(1,1;3/2;t)
=\frac{\arcsin\sqrt t}{\sqrt{t(1-t)}}.
\tag{7}
$$
这里 (7) 只说明原点形式系数，不在模 $p$ 下作解析取值。
一个直接的系数证明是
$$
b_j=\int_0^1(1-v^2)^j\,dv,\qquad
\sum_{j\ge0}b_jt^j
=\int_0^1\frac{dv}{1-t+tv^2}.
$$
这些积分逐个只是有理多项式积分，给 (7) 的同一形式展开。

相应的完整低核微分边界也可保留为
$$
6t(1-t)R_N'-(1+2t)R_N+1
=(3-p)r_Nt^s.
\tag{8}
$$
这是 $\mathbf Q[t]$ 中的准确等式：
低项由
$(6j-1)r_j=(6j-4)r_{j-1}$ 相消，
唯一末项为 $-(6N+2)r_Nt^{N+1}$。
故模 $p$ 的边界为 $3r_Nt^s$，确是单位边界；
它还不是四条原首中央系数中的任何一条。

## 3. 原全卷积的伴随读取

对任意在 $t^0,\ldots,t^N$ 整的实际形式级数 $F$，定义
$$
\mathfrak B_N(F)=\sum_{j=0}^N b_j[t^j]F.
\tag{9}
$$
(5) 逐项给
$$
\boxed{
[t^N](R_NF)=r_N\mathfrak B_N(F)\pmod p.
}
\tag{10}
$$
每个 $b_j$ 均为单位；因此 (10) 没有隐含删除低系数。
它只是将整个原卷积改为一个明确的有限伴随泛函。

现把它放回四条原来源。仍在共同 $b=1$ 模型中写
$$
A_\nu(z)=\Theta(z)^{n_\nu}f_\nu(t(z)),\qquad
(n_\nu)=(17,36,68,33),\qquad f_\nu(t)=tP_\nu(t).
\tag{11}
$$
四个 $f_\nu$ 是 R821 的原完整多项式，
分别对应 $S_{34},T_{72},U_{136},V_{66}$；
不更换它们的任何因子。记
$$
\alpha_\nu=[z^{p+1}]A_\nu=[w^s]A_\nu.
$$
原 Lagrange 公式及 $H(t)^p\equiv1\pmod{t^s,p}$ 给
$$
\alpha_\nu
\equiv6(-1)^s[t^N]H^{-1}(\Theta^{n_\nu}f_\nu)'
\equiv(-1)^s[t^N]\Theta^{n_\nu}P_\nu C H^{-2}.
\tag{12}
$$
第二式可直接用 $6tH'=C-H$ 验证。
特别负角的 $(-1)^s$ 及 $P_\nu=f_\nu/t$ 原常数符号都在。

令
$$
F_\nu=\Theta^{n_\nu}P_\nu/H.
$$
对完整 $F_\nu$ 求导，并用 (4)，得到
$$
6tF_\nu'
=\frac{\Theta^{n_\nu}}H
\left((2n_\nu R-2n_\nu+1)P_\nu+6tP_\nu'
-\frac CH P_\nu\right).
$$
在 $t^N$ 处，$6N\equiv-5\pmod p$，
故 (10)、(12) 给四条原行共同的准确伴随式
$$
\boxed{
\alpha_\nu\equiv(-1)^s\left[
2n_\nu r_N\,\mathfrak B_N\!\left(
\frac{\Theta^{n_\nu}P_\nu}{H}\right)
+[t^N]\frac{\Theta^{n_\nu}}H
\big((6-2n_\nu)P_\nu+6tP_\nu'\big)
\right]\pmod p.
}
\tag{13}
$$
这里所需 $\Theta$ 系数只有 $0,\ldots,N$，
严格在首共振以前，故有原整性。
(13) 保留完整 $\Theta^{n_\nu}$ 指数卷积以及每个原 $P_\nu$。
它不是只有 $r_N$ 的公式，也不是 (9) 对任意输入的非零定理。

回到原 $b=17$ 时，仍按既有准确尺度
$$
A_{\nu,b}(z)=b^{-1}A_{\nu,1}(b^{1/6}z),\qquad
\alpha_{\nu,b}=b^{s-1}\alpha_{\nu,1}.
\tag{14}
$$
本篇没有改变 R821 的 $q_\nu$、Gaussian 或
$pJ_\nu'$ 归一。
R828 中实际 $b_\Theta+a_pB_4v$ 的判定，
仍须将 (13) 按那里的原四行单位尺度代入；
不能省去 (13) 的第二项或其完整低系数。

## 4. 第一个确实闭合的全低卷积

取 (10) 的实际输入 $F=H$。由 (2)、(9) 精确得
$$
\boxed{
[t^N](R_NH)
=r_N\sum_{j=0}^{s-1}
\frac1{(2j+1)(6j+1)}\pmod p.
}
\tag{15}
$$
这不是只保前几个或后几个加数，而是全部 $s$ 项。

记 $\mathsf h_a=\sum_{k=1}^a1/k$，$\mathsf h_0=0$。
部分分式为
$$
\frac1{(2j+1)(6j+1)}
=-\frac1{2(2j+1)}+\frac3{2(6j+1)}.
$$
又因 $1/2\equiv3s$、$1/6\equiv s\pmod p$，
$$
\sum_{j=0}^{s-1}\frac1{2j+1}
=\frac{\mathsf h_{4s-1}-\mathsf h_{3s-1}}2,
\quad
\sum_{j=0}^{s-1}\frac1{6j+1}
=\frac{\mathsf h_{2s-1}-\mathsf h_{s-1}}6.
$$
完整反射
$\mathsf h_{p-1-a}=\mathsf h_a\pmod p$
给 $\mathsf h_{4s-1}=\mathsf h_{2s-1}$。
因此
$$
\boxed{
[t^N](R_NH)
=\frac{r_N}{4}
\big(\mathsf h_{3s-1}-\mathsf h_{s-1}\big)
=\frac{3r_N}{8}q_p(3)\pmod p,
}
\tag{16}
$$
其中始终采用
$$
q_p(3)=\frac{3^{p-1}-1}{p}\in\mathbf Z
\tag{17}
$$
的原 Fermat 商规范，不将它当作已知单位。

### 4.1 调和和到 $q_p(3)$ 的自含定标

取 $\omega^2+\omega+1=0$，令 $\eta=1-\omega$。
因为 $p\equiv5\pmod6$，
$$
\eta^p=(1-\omega^2)R_p^{(3)},\qquad
R_p^{(3)}=-(-3)^{(p-1)/2}.
$$
在原惰性剩余域中 Frobenius 给
$R_p^{(3)}\equiv1\pmod p$，而
$(R_p^{(3)})^2=3^{p-1}$。
因此
$$
R_p^{(3)}\equiv1+\frac p2q_p(3)\pmod{p^2}.
\tag{18}
$$
另一方面，
$\binom pk\equiv p(-1)^{k-1}/k\pmod{p^2}$，
故二项式展开给
$$
\eta^p\equiv
1-\omega^2-p\sum_{k=1}^{p-1}\frac{\omega^k}{k}\pmod{p^2}.
$$
与 (18) 比较，
$$
\sum_{k=1}^{p-1}\frac{\omega^k}{k}
=-\frac{1-\omega^2}{2}q_p(3)\pmod p.
\tag{19}
$$
按 $k\bmod3$ 分组为 $S_0,S_1,S_2$。
变换 $k\mapsto p-k$ 给 $S_1=0,\ S_2=-S_0$，
所以左边为 $(1-\omega^2)S_0$。
该因子为单位，且
$S_0=\mathsf h_{2s-1}/3$，从而
$$
\mathsf h_{2s-1}=-\frac32q_p(3)\pmod p.
\tag{20}
$$
最后把 $\mathsf h_{2s-1}$ 分成奇、偶项：
$$
\mathsf h_{2s-1}
=\frac12\mathsf h_{s-1}
+\frac12(\mathsf h_{4s-1}-\mathsf h_{3s-1}).
$$
再用上面的反射，得到
$\mathsf h_{3s-1}-\mathsf h_{s-1}=-\mathsf h_{2s-1}$。
这与 (20) 正给 (16)，包括 $3/8$ 和全部符号。

## 5. 保留的原问题

(5)–(10) 固定了整个首共振前的反射核，(16) 则支付了一个
原 $R/H$ 的全低卷积，而非其截断近似。
但在 (13) 中，实际输入是
$\Theta^{n_\nu}P_\nu/H$，一般不是 $H$。
尚没有证明四个原 $P_\nu$ 可使这些输入的所有额外项
合成 (15) 或其它已付边界项。
尤其 $q_p(3)$ 本身也没有在本篇被赋为单位。

R828 的实际相容式、完整 $d$-参考运输中的同一
$K_1/C_1$ 及全部 native Schur 项因此继续保留。
本篇没有用原高轴可解、不同 CM 标签、单位 $r_N$、
或一次全卷积闭式，代替四条原首必要系数的共同非零。

依赖：

- [R821](../results/R821-original-four-central-axes-and-complete-four-block-carries.md)：
  原四来源、首共振前整性及完整归一。
- [R828](../results/R828-original-four-high-axis-reflection-and-native-central-compatibility.md)：
  原四高轴和实际 $b_\Theta$/Schur 相容式。
- [完整 $d$-参考运输](2026-11-15-r828-complete-d-reference-transport.md)：
  不改变原源的全部参考和 native 项运输。
- [R595](../results/R595-original-central-diagonals-and-integral-four-row-comparison.md)：
  原全参数留数读取；本篇 (2)、(12) 已明确转换为负角。

全部结论由上述显示的有理恒等式及二项式同余逐项证明。
未作新的目标素数扫描，未生成可重算数值输出。
