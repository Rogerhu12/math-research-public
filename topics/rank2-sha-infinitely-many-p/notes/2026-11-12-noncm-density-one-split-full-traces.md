# 非 CM 的密度一分裂输入、原完整迹与源简单零点

日期：2026-11-12。状态：**以下密度与实际点结论已证明；两步原始性未证明。**

R140 给出不限制分裂型的无穷输入，并保留 \(\widehat h(Q)=o(p)\)。
本篇另造相对密度一的分裂输入，使 R141 的源简单零点与原完整
非挠迹在**同一个选择**上成立；代价是此处高度仅为 \(o(p^2)\)。
没有把两个无穷集合直接相交，也没有把这一高度升级为 R140 的高度。

## 1. 固定对象及结论

固定
\[
 E:y^2+y=x^3+x^2-2x,\qquad F=\mathbb Q(\sqrt{-7}),
 \qquad \pi:X_0(389)\longrightarrow E.
 \tag{1}
\]
使用 R136–R140 的原 Heegner 点、两个最大阶源中心
\(c_+,c_-\)、固定挠点指数 \(t_0\)、非零整数 \(J_m\)，以及
一次固定的模数 \(B_0\)。后者满足
\[
 C\mid B_0,\quad B_0\ge\max\{m_0,3\},\quad 7\mid B_0,
 \qquad C=28\cdot29^k.
 \tag{2}
\]
固定有限模型坏位可吸收进 \(B_0\) 或一次排除。
R140 已证明，对 \(C\mid m,m\ge m_0\)，
\[
 J_m\in\mathbb Z\setminus\{0\},\qquad
                     \log|J_m|\ll m\log(m+2).
 \tag{3}
\]
这些整数同时支付两源中心的真实 period jet；不含随 \(p\) 重新
选择映射或重新选择一个非零分支的量词。

任意固定
\[
                         32/17<\eta<2.
 \tag{4}
\]
设 \(\mathcal P_{-7}\) 是在 \(F\) 分裂的有理素数集合。
则它的一个相对密度一子集中的每个充分大 \(p\) 都能选到原辅助
素数 \(\ell\asymp p^\eta\)，使
\[
 \begin{gathered}
 \ell\equiv-1\pmod{B_0p},\qquad \ell+1=pu,\qquad v_p(\ell+1)=1,\\
 a_p(E)\not\equiv0,\pm1\pmod p,\qquad
 a_\ell(E)\not\equiv0\pmod p,\qquad \ell\nmid J_u.
 \end{gathered}
 \tag{5}
\]
该同一输入的原完整迹
\[
        Q_{p,\ell}=\operatorname{Tr}_{F[\ell]/L}\pi(x_\ell),
              \qquad [L:F]=p,
 \tag{6}
\]
满足
\[
 \begin{gathered}
 Q_{p,\ell}\text{ 非挠},\qquad N_{L/F}Q_{p,\ell}=O,\\
 v_\ell\log_E([t_0]Q_{p,\ell})=1/p,\qquad
 \widehat h(Q_{p,\ell})\ll p^{2\eta-2}\log p=o(p^2),\\
                         Q_{p,\ell}\notin pE(F^{\rm ab}).
 \end{gathered}
 \tag{7}
\]
并且 R141 的实际函数
\[
               g_p=\Theta^{p-2}\bar f/H^p
 \tag{8}
\]
在 \(\bar c_+\)、\(\bar c_-\) 都是简单零点。因此原完整
\(\ell+1\) 方向 Hecke 总迹 \(a_\ell(E)g_p\) 也在这两个源点
有简单零点。

更强地，在 \(p\in(X,2X]\) 的每个典型输入上，能保留
\(\gg X^{\eta-1}/\log X\) 个同时满足上述条件的原 \(\ell\)。
本篇没有声称它们中必有 R139 二阶矩非零者。

## 2. 平均等差下界及一个辅助素数只属于一个输入

Fouvry (2013), §2.6, Lemma 7 是已核读的实际输入。对固定
\(K<17/32\)，对 \(r\sim R<x^K\) 的整数模数，除至多
\(R(\log R)^{-2}\) 个外，固定逆剩余类 \(s^{-1}\) 中
\((x,2x]\) 的素数个数至少
\[
                        \alpha_K\frac{x}{\varphi(r)\log x}.
 \tag{9}
\]
取 \(1/\eta<K<17/32\)、\(x=X^\eta\)、\(R=B_0X\)、
\(r=B_0p\)、\(s=-1\)。因为 \((-1)^{-1}=-1\)，不改变方向。
固定 \(B_0\) 只改变常数；对充分大 \(X\) 有 \(R<x^K\)。

所以除 \(O_{B_0,\eta}(X/\log^2X)\) 个输入素数外，每个
\(p\in(X,2X]\) 都有至少
\[
                  M_X=c_{B_0,\eta}\frac{X^{\eta-1}}{\log X}
 \tag{10}
\]
个候选
\[
         X^\eta<\ell\le2X^\eta,\qquad
                        \ell\equiv-1\pmod{B_0p}.
 \tag{11}
\]
把 (10) 中常数减小即可令此界对整个区间统一。
对这些候选，
\[
 \ell+1<X^2<p^2,
 \qquad \tfrac12X^{\eta-1}<u\le2X^{\eta-1}+1,
 \qquad B_0\mid u.
 \tag{12}
\]
第一式对充分大 \(X\) 成立。它不仅给 \(v_p(\ell+1)=1\)，
还表明同一 \(\ell\) 不会属于两个不同的 \(p\in(X,2X]\)：
否则两个输入素数的乘积整除 \(\ell+1<X^2\)。

这个不重复性允许把所有输入的候选一起计数。它是下面从
全局例外上界转为“每个典型输入仍有好候选”的关键。

## 3. 删除原 jet 坏候选

置 \(U_X=\lceil2X^{\eta-1}+1\rceil\)。由 (3)，
\[
 \log\prod_{\substack{m_0\le m\le U_X\\C\mid m}}|J_m|
                              \ll U_X^2\log U_X.
 \tag{13}
\]
凡 \(\ell\mid J_u\) 的候选都整除 (13) 中的同一个非零整数。
每个这样的素数 \(\ell\) 有 \(\log\ell>\eta\log X\)，故这些
不同坏候选总数为
\[
                            O(X^{2\eta-2}).
 \tag{14}
\]
原实际零迹及非单位首 jet 的候选都包含在 (14) 中，不能反向
把 \(J_u\) 的所有素因子解释成零迹。

## 4. 删除辅助位超奇异候选

Elkies (1991), Theorem B 给固定非 CM \(E/\mathbb Q\) 的
无条件上界
\[
          \#\{\ell\le y:a_\ell(E)=0\}\ll_E y^{3/4}.
 \tag{15}
\]
这里只对**辅助位的零迹**使用它。对 \(a_p=\pm1\) 没有使用
任何这种幂次上界。
代入 \(y=2X^\eta\)，坏辅助素数不超过
\[
                              O(X^{3\eta/4}).
 \tag{16}
\]
其余辅助素数满足 \(a_\ell\ne0\)。又由 Hasse 界及 \(\eta<2\)，
\[
          0<|a_\ell(E)|\le2\sqrt\ell<X<p
 \tag{17}
\]
对充分大 \(X\) 成立，因此它们确实满足 \(a_\ell\not\equiv0\pmod p\)。
本步无需把固定非阿贝尔 Chebotarev 条件附加到 Mikawa 定理。

## 5. 同时保留许多好候选及普通简单源点

由 §2 的不重复性，若一个满足 (10) 的输入损失至少 \(M_X/2\)
个候选，它独占这些坏辅助素数。因此由 (14)、(16)，这种输入数
至多
\[
 \begin{aligned}
 \frac{2}{M_X}\,O\bigl(X^{2\eta-2}+X^{3\eta/4}\bigr)
  &=O\bigl(X^{\eta-1}\log X
                  +X^{1-\eta/4}\log X\bigr)\\
  &=o(X/\log X).
 \end{aligned}
 \tag{18}
\]
剩余每个输入至少有 \(M_X/2\) 个同时避开两类坏集的候选。

在输入 \(p\) 本身，再删除下列集合：

- 固定有限坏集，以及 \(p\mid B_0\)；
- \(a_p(E)\in\{0,\pm1\}\)，其个数由 Thorner–Zaman (2018),
  Theorem 1.4 为 \(O(X(\log\log X)^2/\log^2X)\)；
- \(p\in\mathcal P_{-7}\) 而 R141 的两个源点中有非简单零者，
  其个数为 \(O(X^{3/4})\)。

所有删除都针对同一组输入/候选，合起来的输入例外数为
\[
 O\left(
 \frac{X(\log\log X)^2}{\log^2X}
 +X^{\eta-1}\log X
 +X^{1-\eta/4}\log X
 +X^{3/4}\right)=o(X/\log X).
 \tag{19}
\]
而 \(\#(\mathcal P_{-7}\cap(X,2X])\sim X/(2\log X)\)。
所以在分裂输入中仍为相对密度一。按二进区间求和给通常的
从 \(1\) 到 \(X\) 的相对自然密度结论。

## 6. 原点、局部条件及高度均属于同一选择

取 §5 保留的任一个 \((p,\ell)\)。\(7\mid B_0\) 且
\(\ell\equiv-1\pmod7\)，故 \(\ell\) 在 \(F\) 惰性。
因为 \(h_F=1\)，实际环类群阶为 \(\ell+1=pu\)；
\(p\nmid u\) 给唯一次数 \(p\) 子域 \(L\)，式 (6) 保留全部
\(u\) 项，并非挑选其中一个 Heegner 点。

由 \(B_0\mid u\)、(2) 和 (12)，原 jet 的固定非零进程适用；
\(\ell\nmid J_u\)、\(u<\ell\) 使两中心的 \(b_{c,u}\) 都为
\(\ell\)-单位。R140 §3 的完整尾估计直接给
\(v_\ell\log_E([t_0]Q)=1/p\)，所以 \(Q\) 非挠。
基层 \(P_1=O\) 给准确 \(NQ=a_\ell P_1=O\)。

R140 的固定模映射高度比较以及 (12) 给
\[
 \widehat h(Q)\le u^2\widehat h(P[\ell])
       \ll u^2\log\ell
       \ll p^{2\eta-2}\log p=o(p^2).
 \tag{20}
\]
若 \(Q=pR\)、\(R\in E(F^{\rm ab})\)，则 \(R\) 非挠。
Silverman 的固定全阿贝尔域下界 \(\widehat h(R)\ge c_{E,F}>0\)
与 (20) 矛盾，证明 (7) 的不可除性。

由 (17)，\(\#E(\mathbb F_{\ell^2})\equiv-a_\ell^2\ne0\pmod p\)；
R139 的所有辅助位局部条件及真实范数一族均适用。
于是 \(A(F)\otimes\mathbb Z_p=\mathcal Ow\)、整个 \(\Sha(A/F)\)
有限、\(Q=\delta^a\varepsilon w\)，且其真实 Euler 首项仍为
\(\delta Q\)，长度上界仍为 \(2(a+1)\)。

源简单零性及 \(a_\ell\) 单位由 §5、(17) 同时保证。
实际 Hecke 总迹为 \(a_\ell g_p\)，因此可以直接进入 R141
以后对指定纤维的微分/差分比较，毋须另假设分裂集合的无穷性。

**保留的缺口。** 这里 \(u\asymp p^{\eta-1}\)，一般不能从
(20) 推出 \(o(p)\) 或 R140 的 \(a\le(p-3)/2\)。
源总迹的简单零点也不推出原 \(D_2\) 纤维值非零。
R139 的充分条件仍是同一原点的 \(a\le1\)，尚未证明对无穷
输入成立。

## 原始来源及课题接口

- É. Fouvry，*On binary cyclotomic polynomials*，Algebra & Number
  Theory **7** (2013), 1207–1223，§2.6, Lemma 7，印刷页1212；
  [发表全文](https://msp.org/ant/2013/7-5/ant-v7-n5-p07-p.pdf)。
- N. D. Elkies，*Distribution of supersingular primes*，Astérisque
  **198–200** (1991), 127–132，Theorem B，印刷页131；
  [发表全文](https://www.numdam.org/item/AST_1991__198-199-200__127_0.pdf)。
  此处只用其零迹上界；该文明确说明不依赖 GRH。
- J. Thorner、A. Zaman，*A Chebotarev variant of the Brun–Titchmarsh
  theorem and bounds for the Lang–Trotter conjectures*，IMRN (2018)，
  Theorem 1.4；[作者全文](https://arxiv.org/pdf/1606.09238)。
- [R140 原完整迹、固定29进分支、整数范数及全尾](2026-11-12-noncm-e389-nonzero-small-full-traces.md)。
- [R141 原源点简单零及格点计数](2026-11-12-noncm-fixed-cm-source-simple-zero.md)。
- [R139 真实 Euler 族、所有局部条件及两步充分检验](2026-11-12-noncm-norm-one-system-and-two-step-test.md)。
