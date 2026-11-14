# 非 CM 大素因子的普通、非异常选择

日期：2026-11-12。**已证明。** 本文把已发表的非 CM 固定迹
上界与 Brun–Titchmarsh 配合，证明 R126 的大量大素因子输入
可以删去 \(a_p=0,\pm1\)。没有对非零固定迹使用无条件幂次界，
也没有证明实际 Heegner 点的二次增广非零。

## 1. 一个适用于稀疏素数集的删除引理

设 \(\mathcal B\) 是素数集合，固定常数 \(C\) 使充分大 \(y\) 满足
\[
 A_{\mathcal B}(y):=\#\{q\le y:q\in\mathcal B\}
       \le C\,\frac{y(\log\log y)^2}{(\log y)^2}.
 \tag{1}
\]
固定 \(0<\theta<1\)。则
\[
 \#\{\ell\le x:\ell\text{ 素},\
   \exists p\in\mathcal B,\quad p>x^\theta,\quad p\mid\ell+1\}
 \ll_{\theta,C}
       \frac{x(\log\log x)^2}{(\log x)^{3/2}}
 =o(x/\log x).
 \tag{2}
\]
任何额外固定等差限制只缩小待删集合，故同一上界适用。

### 1.1. 倒数和

分部求和给
\[
 \begin{aligned}
 \sum_{\substack{x^\theta<p\le x\\p\in\mathcal B}}\frac1p
 &\le \frac{A_{\mathcal B}(x)}x+
      \int_{x^\theta}^{x}\frac{A_{\mathcal B}(t)}{t^2}\,dt\\
 &\ll_{\theta,C}\frac{(\log\log x)^2}{\log x}.
 \end{aligned}
 \tag{3}
\]
例如把 \((\log\log t)^2\) 以上界 \((\log\log x)^2\) 代替，
再用 \(\int dt/[t(\log t)^2]
 =-1/\log t\)，就得到所写的统一常数。

### 1.2. 远离 \(x\) 的因子

令 \(L=\sqrt{\log x}\)。当
\[
             x^\theta<p\le xe^{-L},
\]
Brun–Titchmarsh 给
\[
 \#\{\ell\le x:\ell\text{ 素},\ \ell\equiv-1\pmod p\}
 \le\frac{2x}{(p-1)\log(x/p)}
 \ll\frac{x}{pL}.
 \tag{4}
\]
对坏 \(p\) 求和并使用 (3)，该部分至多
\[
       O_{\theta,C}
       \left(\frac{x(\log\log x)^2}{(\log x)^{3/2}}\right).
 \tag{5}
\]

### 1.3. 接近 \(x\) 的因子

若 \(p>xe^{-L}\)，写 \(\ell+1=up\)，则
\[
       1\le u\le2e^L.
\]
忽略 \(\ell=up-1\) 的素性，只计 \(p\in\mathcal B\)。
对所有这些 \(u\)，参数
\[
 y_u=(x+1)/u\ge\tfrac12x e^{-L}
\]
满足 \(\log y_u=\log x+O(\sqrt{\log x})\)，所以 (1)
统一给
\[
 \begin{aligned}
 \sum_{u\le2e^L}A_{\mathcal B}((x+1)/u)
 &\ll_C\frac{x(\log\log x)^2}{(\log x)^2}
               \sum_{u\le2e^L}\frac1u\\
 &\ll_C\frac{x(\log\log x)^2}{(\log x)^{3/2}}.
 \end{aligned}
 \tag{6}
\]
这也覆盖端点可能的 \(p\le x+1\)。结合 (5)–(6) 得 (2)。
整个证明是上界；重复计数只增大上界，不需唯一分解条件。

## 2. 固定非 CM 曲线的三个坏迹

固定任意非 CM 椭圆曲线 \(E/\mathbb Q\)。Thorner–Zaman
发表版 Theorem 1.4（作者版 §1，式 (1.16)–(1.17) 后；
§9.1 给证明）对每个固定整数 \(a\) 证明
\[
       \#\{p\le y:p\nmid N_E,\ a_p(E)=a\}
       \ll_E \frac{y(\log\log y)^2}{(\log y)^2}.
 \tag{7}
\]
必须保留其前置的 **非 CM** 假设。对 \(a=0,1,-1\) 求和，
再加入任意固定有限例外集，满足 (1)。因此 (2) 可以删除所有
\[
       a_p(E)\in\{0,1,-1\}.
 \tag{8}
\]
当 \(p\ge7\) 时，Hasse 界 \(2\sqrt p<p-1\) 说明
\[
 a_p\notin\{0,\pm1\}
 \quad\Longrightarrow\quad
 a_p\not\equiv0,\pm1\pmod p.
 \tag{9}
\]
于是留下的 \(p\) 普通，且 \(1-a_p\)、
\((p+1)^2-a_p^2\) 都是 \(p\)-单位。

这里没有把超奇异素数的特殊幂次上界套到 \(a_p=\pm1\)。
仅用粗估计 \(x\sum_{p\in\mathcal B}1/p\) 会丢掉 (4) 的
素性节省，不能由 (7) 得到所需的 \(o(x/\log x)\)；
上面两段处理保留了这一层。

## 3. 与真正大因子集合相交

固定整数 \(B\)。R126 已证明（含 Fouvry 1985 原文勘误、
固定进程和纯有理积分证书），取
\[
            \theta=667/1000
\]
有常数 \(c_B>0\)，使充分大 \(x\) 满足
\[
 \#\{\ell\le x:\ell\text{ 素},\
          \ell\equiv-1\pmod B,\
          P^+(\ell+1)>x^\theta\}
            \ge c_B x/\log x.
 \tag{10}
\]
对 (10) 里的 \(p=P^+(\ell+1)\) 应用 (2)，只删去
\(o(x/\log x)\) 个 \(\ell\)。同时可以再删掉
\(a_\ell(E)=0\) 的 \(\ell\)：直接用 (7) 的 \(a=0\)
上界就已经是 \(o(x/\log x)\)，不必调用更强的 Elkies 界。
因此仍有
\[
 \gg_B x/\log x
 \tag{11}
\]
个实际 \(\ell\)，同时满足
\[
 \begin{gathered}
 \ell\equiv-1\pmod B,\qquad p=P^+(\ell+1)>x^{667/1000},\\
 a_p(E)\notin\{0,\pm1\},\qquad a_\ell(E)\ne0.
 \end{gathered}
 \tag{12}
\]
固定有限素数和所有与 \(N_EB\) 相交的例外都可删除。
由于 \(p>x^\theta\)，所得到的 \(p\) 不可能落在固定有限集，
所以有无穷多个不同的 \(p\)。

对充分大 \(x\)，
\[
 2\sqrt\ell\le2\sqrt x<x^\theta<p,
\]
从而 (12) 的 \(a_\ell\) 自动是模 \(p\) 的非零元。
又因 \(p^2>x^{2\theta}>x+1\)，有
\[
 v_p(\ell+1)=1,\qquad
 u=(\ell+1)/p\ll p^{333/667},\qquad u^2=o(p).
 \tag{13}
\]
最后一式由 \(x<p^{1000/667}\) 直接推出。

## 4. 对固定 E389 的准确算术后果

R136 已独立证明
\[
 E:y^2+y=x^3+x^2-2x,\qquad F=\mathbb Q(\sqrt{-7})
\]
的秩至少二、非 CM 性，负七扭曲解析秩一与整个 Sha 有限，
以及实际基层 Heegner 点 \(P_1=O\)。

在 (10) 中可令固定 \(B\) 被 \(7\) 整除，并加入所有所需的
固定进程因子。由于 \(\ell\equiv-1\pmod7\)，
\(\chi_{-7}(\ell)=(\ell/7)=-1\)，所以 \(\ell\) 在 \(F\)
惰性。又 \(h_F=1\)，实际环类群的阶是 \(\ell+1\)，
其唯一次数 \(p\) 商 \(L/F\) 由 (13) 给出。

局部于 \(\ell\)，\(F_\ell/\mathbb Q_\ell\) 是不分歧二次扩张，
而
\[
 \#E(\mathbb F_{\ell^2})=(\ell+1)^2-a_\ell^2
                 \equiv-a_\ell^2\not\equiv0\pmod p.
 \tag{14}
\]
因此 \(E[p]\) 在该处的 Frobenius 没有特征值 \(1\)。
因为剩余域大小 \(\ell^2\equiv1\pmod p\)，局部 Tate
对偶也给 \(H^2(F_\ell,E[p])=0\)。Euler–Poincaré
特征式（\(\ell\ne p\)）于是给
\[
                 H^1(F_\ell,E[p])=0.
 \tag{15}
\]
也可从不分歧表示的 tame inertia 正合列直接看出：不分歧
部分是 \(E[p]/(\operatorname{Frob}_{\ell^2}-1)E[p]=0\)，
分歧部分为 \(E[p]^{\operatorname{Frob}_{\ell^2}=\ell^2}=0\)。
故 (15) 不只是有限条件的零性。

对首项实际完整迹
\[
             Q=\operatorname{Tr}_{F[\ell]/L}\pi(x_\ell)
\]
有
\[
           N_{L/F}Q=a_\ell P_1=O.
 \tag{16}
\]
这不意味着所有辅助层也具有同样的范数零性：
\(N_\Gamma Y_n=a_\ell P_n\) 中的 \(P_n\) 未必为零。
目前安全的 norm-one Euler 族首项是 \((\tau-1)Q\)，
不能删去它多出的一层 \(\delta\)。

这些 \(p\) 的 ordinary/nonanomalous 性已付清，但 **没有**
另外要求 \(p\) 在 \(F\) 分裂，也没有由 (11)–(16) 宣称
\(Q\) 非挠、\(\delta^2\) 不整除 \(Q\) 或原曲线初级 Sha 有限。
完整点的非零选择和实际 Selmer 上界还须各自证明。

## 一手来源与审查

- J. Thorner、A. Zaman，
  *A Chebotarev variant of the Brun–Titchmarsh theorem and bounds
  for the Lang–Trotter conjectures*，
  IMRN **2018** (16), 4991–5027。
  [作者全文](https://arxiv.org/pdf/1606.09238)，
  Theorem 1.4、§9.1；(1.4) 同时准确列出这里使用的
  Montgomery–Vaughan Brun–Titchmarsh 上界。
  前置非 CM 假设在作者版印页 4 的 (1.15) 前后。
- R126 的固定进程大素因子定理及勘误证书；本文只做稀疏
  集合的上界删除，保留它的 \(\theta=667/1000\)。
- R136 的原曲线、负扭曲、类数一 Heegner 域和基层点；
  这里没有重新假设 \(E\) 的秩上界或无穷素数结论。
- 分部求和、两段参数、实际 local \(H^1=0\) 均在本文证明。
  两段删除估计已由另一代理独立复算通过。
