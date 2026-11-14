# 实际零矩的稀疏性与显式辅助模数 1020p

日期：2026-11-12。状态：完整证明；R123。环境恢复后依据已独审文本重建。

R116 已用实际固定 ordinary 盘和 Cornut 定理证明一个指定 Mellin 分支不恒为零。
本篇使用这个**实际**非零分支，证明其全矩的零指标十分稀疏，进而去掉辅助进程中
未知的 \(61\) 幂。不把任意非零形式级数当作此非零输入。

## 1. 实际固定分支给出的零矩约束

固定 \(q=61\)。对 R116 的有限 CM 中心集合 \(\Sigma\)，已有整有界测度 \(\mu_c\)，
\[
 \int_{\mathbb Z_q}x^{m-1}\,d\mu_c(x)=\kappa_c^m h_{c,m},
 \qquad h_{c,m}=m!b_{c,m},\quad \kappa_c\ne0.
 \tag{1}
\]
所用分支
\[
 M_c(W)=\int_{\mathbb Z_q^\times}x^{-1}
       (1+W)^{\log\langle x\rangle/\log(1+q)}\,d\mu_c(x)
          \in\mathcal O_{\mathbb C_q}[[W]]
 \tag{2}
\]
不恒为零。令
\[
                         f_c(z)=M_c(62^z-1),\qquad z\in\mathbb Z_{61}.
 \tag{3}
\]
由于 \(\log62\in61\mathbb Z_{61}^{\times}\)，\(62^z-1\) 在 Tate 代数中的
Gauss 范数至多 \(1/61\)。外层 \(M_c\) 的系数有界，所以 (3) 属于
\(\mathbb C_{61}\langle z\rangle\)。形式复合的内层有非零一次项，故复合单射：
\[
                              f_c\ne0.
 \tag{4}
\]

若 \(60\mid m\)，单位上的 Teichmüller 部分恰好消去，因而
\[
 f_c(m)=\int_{\mathbb Z_{61}^{\times}}x^{m-1}\,d\mu_c(x),\qquad
 v_{61}\left(\int_{61\mathbb Z_{61}}x^{m-1}\,d\mu_c(x)\right)\ge m-1.
 \tag{5}
\]
因此
\[
      60\mid m,\ h_{c,m}=0\quad\Longrightarrow\quad v_{61}f_c(m)\ge m-1.
 \tag{6}
\]
这里仅用了 \(\kappa_c\ne0\)，没有将未指定的周期常数当作整单位。

## 2. 一个受限解析函数的指数间距引理

**引理。** 设非零 \(f\in\mathbb C_q\langle z\rangle\)。固定常数 \(C\)。
正整数集合
\[
 \mathcal Z=\{m\ge1:v_q f(m)\ge m-C\}
 \tag{7}
\]
在每个固定比例窗口 \([aU,bU]\)，\(0<a<b\)，中至多有 \(O_{f,C,a,b}(1)\) 个元素。
而对任意 \(s>0\)，\(\sum_{m\in\mathcal Z}m^{-s}<\infty\)。

**证明。** 这里只使用 \(\mathbb Z_q\) 的紧性，不使用 \(\mathbb C_q\) 单位球的紧性。
Strassmann 定理或解析零点的孤立性给出 \(f\) 在 \(\mathbb Z_q\) 中只有有限个零点
\(\alpha_1,\ldots,\alpha_r\)。在每个零点附近取足够小的球，使
\[
 f(z)=(z-\alpha_i)^{d_i}g_i(z),\qquad |g_i(z)|_q
       \text{ 在该球上为非零常数}.
 \tag{8}
\]
这些球的补集在 \(\mathbb Z_q\) 中紧且无零点，所以其上 \(v_q f\) 有上界。
故充分大的 (7) 中整数必须落入某个球，并满足
\[
                     v_q(m-\alpha_i)\ge(m-B_i)/d_i.
 \tag{9}
\]
恰等于某个整数零点的 \(m\) 只有有限个，单独保留即可。
两个不同正整数 \(m<n\) 若分配给同一个 \(\alpha_i\)，则
\[
 v_q(n-m)\ge(m-B_i)/d_i,\qquad
                     n-m\ge q^{(m-B_i)/d_i}.
 \tag{10}
\]
后一式是整数整除所给的通常实数大小下界。
对 \(m,n\in[aU,bU]\)，(10) 与 \(n-m\le(b-a)U\) 在充分大 \(U\) 时矛盾。
故每个零点最终最多贡献一个指标；有限初始区间吸入常数。
在二进窗口上求和立即得到任意 \(s>0\) 的级数收敛。证毕。

应用于每个 (3)，再对固定有限 \(\Sigma\) 取并集，得到
\[
 \mathcal B=\{m\ge1:60\mid m,\ \exists c\in\Sigma,\ h_{c,m}=0\}
 \quad\Longrightarrow\quad
             \#(\mathcal B\cap[aU,bU])=O(1).
 \tag{11}
\]
没有要求这些解析零点或阈值已被有效计算。

## 3. 直接使用显式模数 1020p

固定 \(32/17<\theta<2\)，取输入 \(p\in(X,2X]\cap\mathcal P_F\)。
对除 \(O(X/\log^2X)\) 个输入以外，Mikawa–Fouvry 给
\[
 \gg X^{\theta-1}/\log X
 \quad\text{个}\quad
 X^\theta<\ell\le2X^\theta,\qquad \ell\equiv-1\pmod{1020p}.
 \tag{12}
\]
令 \(u=(\ell+1)/p\)。此时
\[
 60\mid u,\qquad \tfrac12X^{\theta-1}\le u\le2X^{\theta-1}+1,\qquad
 p^2>\ell+1.
 \tag{13}
\]
所有出现的 \(u\) 位于一个固定比例窗口。(11) 说其中使任一实际中心的
\(h_{c,u}\) 为零的指标只有 \(O(1)\) 个。
对每个固定 \(u\)，由 \(\ell=pu-1\)，最多有 \(O(X)\) 个区间内输入；
因此这些**真零指标**总共删除 \(O(X)\) 个候选。

对剩余的 \(u\)，R116 的固定多项式微分系统给非零整范数乘积
\[
 J_u=\prod_{c\in\Sigma}N_{K/\mathbb Q}(A^{du+1}h_{c,u}),\qquad
                         \log|J_u|\ll u\log(u+2).
 \tag{14}
\]
实际首 jet 非单位必有 \(\ell\mid J_u\)。令 \(U=\lceil2X^{\theta-1}+1\rceil\)，则
\[
 \log\prod_{\substack{u\le U\\u\notin\mathcal B,\ 60\mid u}}|J_u|
                   =O(U^2\log U).
 \tag{15}
\]
每个坏候选 \(\ell>X^\theta\) 耗用 (15) 中一个不同素因子，故这部分只有
\(O(X^{2\theta-2})\) 个。
又因 \(\theta>32/17>3/2\)，真零指标的 \(O(X)\) 已被该数量级吸收。
一个候选 \(\ell\) 仍不可能属于两个区间内输入 \(p\)，所以全部候选都坏的输入至多
\[
 O(X^{\theta-1}\log X)=o(X/\log X).
 \tag{16}
\]
这正好恢复 R116 的密度一结论，并将其辅助模数替换为明确的 \(1020p\)。

## 4. 同时保留其他已付条件

对选中的同一个 \(\ell\)，R114 的精确迹公式给首局部赋值 \(1/p\)。
R107 的 abelian 挠点结论使实际非零 \(Q\) 非挠；R110 的高度 \(o(p^2)\)
和 Baker 下界使它不属于 \(pE(F[\ell])\)。
R121 的正局部化坏集合仍只有 \(O(U^2/\log X)\)，也可同时删除。
因而密度一输入可满足
\[
 \begin{gathered}
 \ell\equiv-1\pmod{1020p},\quad v_p(\ell+1)=1,\quad
 Q_{p,\ell}\ne O,\quad Q_{p,\ell}\notin pE(F[\ell]),\\
 v_\ell\log_E([2]Q_{p,\ell})=1/p,\qquad r_+=1.
 \tag{17}
 \end{gathered}
\]
对有限条有同样实际 ST/Cornut 非零分支的固定曲线，可对全部中心取有限并集，
证明完全相同；R124 使用这一有限并版本。

显式的是模数 \(1020p\)，不是所有阈值的数值有效性。
这也没有使实际 \(Q\) 的 \(\delta\) 整除指数为零。

## 5. 一手依据

- 实际 (1)–(2) 的非零及整测度：
  [R116](../results/R116-density-one-nonzero-full-heegner-traces.md) 及其三份完整证明。
- 完备非阿基米德域中的受限幂级数、解析零点和 Strassmann：
  K. Conrad，[Infinite series in p-adic fields](https://kconrad.math.uconn.edu/blurbs/gradnumthy/infseriespadic.pdf)，§§7、10；
  [Strassmann's theorem and an application](https://kconrad.math.uconn.edu/blurbs/gradnumthy/strassmannapplication.pdf)。
  此处特别保留紧集是 \(\mathbb Z_{61}\) 的事实。
- 固定模数的解析素数输入：
  [R110](../results/R110-density-one-small-heegner-auxiliary-primes.md)，引用已核的
  Fouvry, *On binary cyclotomic polynomials*, Lemma 7。

