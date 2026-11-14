# R602：实际正根号族的中心均值、明确秩零区域和本原选择

日期：2026-11-14。状态：**本文充分条件全部证明；其外的实际候选仍 OPEN。**

原未推 R602 的完整字节在工作区丢失后不可用。本稿从已经恢复并发布的 R587、R598、R600 重新推导。恢复过程中把原记录中的充分区域 \(p/D\ge64+8\log(1+\log D)\) 加强为下文 (602.2)；这是有独立复核的新加强，不冒认旧字节或旧证书。

## 1. 准确对象与结论

设 \((p,d)\) 来自 R317 的实际偶分支：\(p>37\)、\(p\equiv2,5\pmod9\)，\(d\) 为其立方自由参数，\(d\) 奇、\(3\nmid d\)、\(d\equiv\pm1\pmod9\)。令 \(D\) 为 \(d\) 在 \(2,3,p\) 之外的素支撑之积，令 \(s(D)\) 为其中惰性素数的个数。本文假设 \(s(D)\) 奇数。

[R587](R587-actual-even-conductor-and-root-number.md) 已确定同一实际族

\[
g_{k,d}=\operatorname{AI}_{K/\mathbb Q}
 (\Psi\theta_k\kappa_4\kappa_d^{-1}),\quad
K=\mathbb Q(\zeta_3),\quad
k\equiv5\pmod6,
\tag{602.1}
\]

具有准确水平 \(108p^2D^2\)、根号 \(+1\)。不把 \(\kappa_4^{-1}\) 独立族代入。由 R604，当前实际正根号支还满足 \(D\ge65\)。取

\[
\mathcal L=1+\log D,\quad r=p/D,\quad h=(p+1)/6.
\]

**定理 602.1。** 若

\[
\boxed{r\ge40+\frac{20}{3}\log\mathcal L,}
\tag{602.2}
\]

则

\[
\boxed{\frac1h\sum_{k\equiv5\ (6)}L(g_{k,d},1)
 >\frac1{\mathcal L}.}
\tag{602.3}
\]

因此至少一个实际 \(\mathbb Q\)-单因子 \(A_{k,d}\) 满足
\(\operatorname{rank}A_{k,d}(\mathbb Q)=0\)。本句尚不保证它是指定的 \(\theta_{-1}\) 因子。

对指定因子，令

\[
q_{p+1}=1-\frac{3\varphi(p+1)}{p+1},\qquad
B_0=2\sqrt{3\sqrt3\,pD}.
\tag{602.4}
\]

在 (602.2) 之外再假设

\[
\boxed{q_{p+1}B_0\le1/\mathcal L,}
\tag{602.5}
\]

则同一个实际 \(A_{-1,d}\) 有秩零。特别地，以下是足够的可检查情形：

1. \(p+1=3\cdot2^\nu\)，且 (602.2) 成立；
2. \(p+1=6\ell\)、\(\ell\) 为素数，且 \(p/D\ge1000\mathcal L^2\)。

这些是对实际候选的条件定理，没有声称符合第二种形状的素数无限，也没有给变化 \(D\) 的统一上界。

## 2. 中心公式与真实平均的两条直线

记

\[
c=\frac\pi{3\sqrt3},\qquad
 t=\frac c{pD}=\frac{2\pi}{\sqrt{108p^2D^2}},\qquad
 A=\frac{cp}{4D},\qquad
 \mathcal Q(x)=\frac{e^{-x}}{1-e^{-3x}}.
\tag{602.6}
\]

对根号为正的权二形式，把 Mellin 积分在自对偶点分开并用函数方程，得到绝对收敛的中心公式

\[
L(g_{k,d},1)=2\sum_{n\ge1}\frac{a_n(g_{k,d})}{n}e^{-tn}.
\tag{602.7}
\]

此公式在本准确水平成立，允许偶水平。系数关于 \(k\) 的依赖和真正 tame 限制仍是 R598 §3 的完整 \(\Theta_p=\{k\equiv5\pmod6\}\)。角色正交平均及六个单位旋转只留下

\[
L_R:\ \alpha=a+b\zeta_3,\ b\equiv0\pmod p,
\qquad
L_I:\ 2a-b\equiv0\pmod p.
\tag{602.8}
\]

有理精确射线的真实相位为正；纯虚精确射线被 3 处导子删掉，不产生抵消主项。令 \(\chi=\chi_{-3}\)，

\[
F_M(t)=\sum_{\substack{n\ge1\\(n,M)=1}}
 \frac{\chi(n)}n e^{-tn^2}.
\tag{602.9}
\]

有理射线贡献正好 \(2F_{2pD}(t)\)。其余格点的范数分别为

\[
(a-pb/2)^2+3p^2b^2/4\quad(b\ne0),
\qquad
p^2k^2/4+3b^2/4\quad(k\ne0,\ b\equiv k\pmod2).
\tag{602.10}
\]

用与 R598 相同的完整格点求和，而将导数核 \(E_1(x)\) 换为本篇的 \(e^{-x}\)，得到

\[
\left|\frac1h\sum_k L(g_{k,d},1)-2F_{2pD}(t)\right|
 \le E_{\rm off}^{(0)},
\tag{602.11}
\]

\[
E_{\rm off}^{(0)}=
\frac4p\left[
 \left(\frac1{\sqrt3}+3^{1/4}\sqrt{pD}\right)\mathcal Q(3A)
 +\left(1+3^{1/4}\sqrt{pD}\right)\mathcal Q(A)
\right].
\tag{602.12}
\]

具体地，先用 (602.10) 的横向正距离界 \(|\alpha|^{-1}\)，再用
\(\sum_{n\in\mathbb Z}e^{-u(n+v)^2}\le1+\sqrt{\pi/u}\)
控制横向高斯和。纵向使用 \(j^2\ge1+3(j-1)\)，分别得到 \(\mathcal Q(3A)\) 与 \(\mathcal Q(A)\)。第二直线的 \(b\) 步长为二；两处尺度因此都准确给 \(3^{1/4}\sqrt{pD}\)。这里没有对本原子族沿用范数 \(p^2/4\) 下界；本原处理另在第 6 节。

## 3. Poisson 主项及全部 Euler 因子

R598 (598.18)–(598.19) 的直接 Poisson 恒等式为

\[
F_1(t)=c-\frac\pi{\sqrt3}
 \sum_{n\ge1}\chi(n)\operatorname{erfc}
   \left(\frac{\pi n}{3\sqrt t}\right),
\]

\[
|F_1(t)-c|\le\sqrt{\frac{3t}{\pi}}
 \mathcal Q\left(\frac{\pi^2}{9t}\right).
\tag{602.13}
\]

取 \(M=2D\)，完整包含排除给

\[
F_M(t)=\sum_{e\mid M}\frac{\mu(e)\chi(e)}e F_1(te^2)
       =cP_M+\delta_M,
\quad
P_M=\prod_{q\mid M}\left(1-\frac{\chi(q)}q\right).
\tag{602.14}
\]

由 \(e\le2D\)、\(\tau(2D)\le2D\) 以及
\(\pi^2/(9t(2D)^2)=3A\)，严格得到

\[
|\delta_M|\le 2\,3^{-1/4}r^{-1/2}\mathcal Q(3A).
\tag{602.15}
\]

\(p\) 不整除 \(M\) 且 \(\chi(p)=-1\)，故删除表示素数的 Euler 因子给

\[
F_{2pD}(t)=F_M(t)+p^{-1}F_M(tp^2),
\qquad
\frac2p|F_M(tp^2)|\le\frac2p\mathcal Q(4A).
\tag{602.16}
\]

最后一个界直接删去互素及角色限制，用 \(n^{-1}\le1\) 和 \(n^2\ge1+3(n-1)\)。没有未经证明把第二项当正数。

分裂素数可能使 \(P_M\) 变小，因此保留其真实损失。由于 \(D\) 奇，

\[
P_M\ge\frac32\prod_{q\mid D}(1-1/q)
 \ge\frac3{2\zeta(2)\mathcal L}.
\tag{602.17}
\]

后一个不等式由
\(\prod_{q\mid D}(1-1/q)^{-1}
 \le\zeta(2)\sum_{e\mid D}1/e
 \le\zeta(2)(1+\log D)\)
直接证明。于是主项严格满足

\[
2cP_M\ge\frac6{\pi\sqrt3\,\mathcal L}
 >\frac{12}{11\mathcal L}.
\tag{602.18}
\]

## 4. 加强后的有效区域

由 (602.11)、(602.15)、(602.16)，令

\[
E=E_{\rm off}^{(0)}+
4\,3^{-1/4}r^{-1/2}\mathcal Q(3A)+\frac2p\mathcal Q(4A).
\tag{602.19}
\]

只要 \(A>6\)，就有 \(\mathcal Q(kA)<2e^{-kA}\le2e^{-A}\)，因而

\[
E<\left[\frac{20}p+
 \frac{16\,3^{1/4}+8\,3^{-1/4}}{\sqrt r}\right]e^{-A}
 <\left(\frac{20}p+\frac{40}{\sqrt r}\right)e^{-A}.
\tag{602.20}
\]

这是本次加强的关键：此粗界不需要旧恢复记录中更强的 \(A>8\)。由于 \(c>3/5\)，(602.2) 蕴含

\[
A>6+\log\mathcal L.
\]

又 \(p\ge41\)、\(r\ge40\)，所以 \(20/p<1/2\)、\(40/\sqrt r<20/3\)。用 \(e^6>400\)（也可由 R600 保存的有理 Taylor 下界平方取得），得到

\[
E<\frac{43}{2400\mathcal L}.
\tag{602.21}
\]

因此

\[
\frac1h\sum_kL(g_{k,d},1)
 >\frac1{\mathcal L}
 \left(\frac{12}{11}-\frac{43}{2400}\right)
 =\frac1{\mathcal L}
 \left(1+\frac{1927}{26400}\right)
 >\frac1{\mathcal L}.
\tag{602.22}
\]

证明 (602.3)。所有常数均有精确有理余量；本结论没有由有限素数扫描外推。

## 5. 非消失因子的实际秩零

由正均值至少一个实际形式满足 \(L(g_{k,d},1)\ne0\)。使用已发布的
[任意水平 Heegner 秩接口](general-level-Heegner-rank-interface.md) 的正根号版本，得到其实际有理单因子秩零。

该接口的量词是：BFH Introduction Theorem (i) 给满足全部水平分裂条件的虚二次扭曲且导数非零；辅助域可避开原 CM 域。Gross–Zagier 与 Nekovář 给辅助域上的一个 Heegner \(F\)-直线，Fricke 下降 \(\bar P=-\epsilon P=-P\) 使整个直线反不变，从而有理不变部分为零。这里没有把仅对奇水平的命题无条件扩用到偶水平，也没有对超越的 \(L\) 值假定代数 Galois 作用。

## 6. 指定本原轨道

各 CM 系数满足 \(|a_n|\le a_K(n)\sqrt n\)，其中 \(a_K(n)\) 为范数 \(n\) 的整理想数。R598 的六角格点论证给 \(A_K(X)=\sum_{n\le X}a_K(n)\le X\)。对递减函数 \(x^{-1/2}e^{-tx}\) 作 Stieltjes 分部积分，因此

\[
|L(g_{k,d},1)|\le2\sum_{n\ge1}a_K(n)n^{-1/2}e^{-tn}
\le2\int_0^\infty x^{-1/2}e^{-tx}\,dx
=2\sqrt{3\sqrt3\,pD}=B_0.
\tag{602.23}
\]

R600 已证明在完整 \(\Theta_p\) 中本原角色比例为
\(\kappa_{p+1}=3\varphi(p+1)/(p+1)\)，且所有本原角色恰属于指定实际 \(A_{-1,d}\) 的同一有理 Galois 轨道。由 (602.3) 和 (602.23)，本原角色的总中心值严格大于

\[
h\left(\mathcal L^{-1}-q_{p+1}B_0\right).
\tag{602.24}
\]

(602.5) 使其严格为正。故该同一实际因子中至少一个形式中心非零，应用第 5 节秩接口得到 \(\operatorname{rank}A_{-1,d}(\mathbb Q)=0\)。

当 \(p+1=3\cdot2^\nu\)，\(q_{p+1}=0\)。当 \(p+1=6\ell\)、\(\ell\) 素，\(q_{p+1}=1/\ell\)，并且

\[
\frac{B_0}{\ell}
 =\frac{12\sqrt{3\sqrt3\,pD}}{p+1}
 <\frac{12\sqrt{3\sqrt3}}{\sqrt r}.
\tag{602.25}
\]

若 \(r\ge1000\mathcal L^2\)，则 \(432\sqrt3<1000\) 保证右端小于 \(1/\mathcal L\)。同时 \(\log\mathcal L\le\mathcal L-1\) 和 \(\mathcal L\ge1\) 使该条件蕴含 (602.2)。定理的两种具体情形遂全部证明。

## 7. 与真实局部排除的边界

本条给的是同一实际商的全局秩零条件。它尚未证明指定 CM 系数 \(M_0\) 为单位，未由 \(c_1\) 到 \(c_0\) 偷换曲线上的点，也没有在正秩商上把阿贝尔首项唯一零误当二次高度唯一零。

R603 将把本条指定 \(A_{-1,d}\) 的秩零、R597 的真实扭曲图式、R592 的完整尾界和经 R588/R589 证明的实际 \(c_0\) 单位条件组合。一般本原 Möbius 误差、单位系数的全素数非消失以及本区域之外的变化 \(d\) 仍开放，绝对 Serre 一致性未完成。
