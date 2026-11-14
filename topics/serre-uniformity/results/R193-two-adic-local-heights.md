# R193：固定 CM 切向参数下，54 个 Hecke 高度的 2 处项

日期：2026-11-13（台北）；未推送结果的第二次恢复版本。
输入为已推送的 R190 证书。旧临时文件已经丢失，本文与程序采用重建后的真实 SHA。

## 1. 对象与结论

沿用 R186/R190：\(X=X_{\rm ns}^{+}(41)\)，
\(B=Z_{-4}-D_{\rm cusp}\)，两个有效除子的次数均为 20。
CM 点采用切向参数 \(j-1728\)，尖点采用 \(q_{41}\)；
局部估值满足 \(v_2(2)=1\)。\(T_n\) 计所有阶为 \(n\) 的子群，
故 \(\deg T_n=\sigma_1(n)\)，不是只计循环子群。
特殊标签 \(C_4=T_4-T_1=T_2^2-3T_1\)。

将特征 2 的极大阶写成 Hurwitz 阶
\[
 {\cal H}=\{(a+bi+cj+dk)/2:a,b,c,d\in\mathbf Z,\
 a\equiv b\equiv c\equiv d\pmod2\},\qquad i^2=j^2=-1,\quad ij=-ji.
\]
记 \(\rho(n)=\frac14\#\{\alpha\in\mathbf Z[i]:N\alpha=n\}\)。
对 \(\beta=(a+bi+cj+dk)/2\)、\(N\beta=n\) 且 \((c,d)\ne(0,0)\)，令
\[
 L(\beta)=v_2(c^2+d^2),\qquad
 w(\beta)=
 \begin{cases}
 20,&a=b=0,\\
 1,&-(a^2+b^2)(c^2+d^2)\text{ 在 }\mathbf F_{41}\text{ 中为非平方},\\
 0,&\text{其余}.
 \end{cases}
\]
为定义层质量，在 Gaussian 元素上另置 \(w=20\)。

**结论。** 对本课题每个普通 Hecke 标签，
\[
 \boxed{I_2(B,T_nB)=
 \frac14\sum_{\substack{\beta\in{\cal H}\\N\beta=n\\(c,d)\ne(0,0)}}L(\beta)w(\beta)
 +20\rho(n)v_2(n)-120\rho(n).} \tag{1}
\]
对 \(C_4\) 以双线性相减。特别地：

| 对应 | \(T_1\) | \(T_2\) | \(T_3\) | \(C_4\) |
|---|---:|---:|---:|---:|
| \(I_2\) | \(-80\) | \(-40\) | \(0\) | \(80\) |

枚举核实有限算术输入；下面的变形与粗模论证确定几何归一化。

## 2. 项链权重与四单位除数

取 \(\sqrt{-1}=9\in\mathbf F_{41}\)。二倍坐标对应矩阵
\[
 \beta\longmapsto
 \begin{pmatrix}A&B\\C&D\end{pmatrix}
 =\frac12\begin{pmatrix}a+9b&c+9d\\-c+9d&a-9b\end{pmatrix}. \tag{2}
\]
行列式为 \(n\)，本题所有 \(n\) 均与 41 互素。
20 个被射影 \([i]\) 固定的无向项链可标为
\[
 J_t=\begin{pmatrix}0&t\\1&0\end{pmatrix},\qquad
 t\in\mathbf F_{41}^{\times}\text{ 非平方}.
\]
\(\beta\) 把此项链送到另一个 \([i]\)-固定项链，当且仅当
\[
 BD-ACt=0. \tag{3}
\]
Gaussian 与 anti-Gaussian 情形给出全部 20 个解；其余情形至多一个。
该解为非平方的判据恰为 (1) 中的二次特征，故 \(w\) 为实际匹配数。

枚举包括 \(\beta,-\beta\) 和全部四个 Gaussian 单位的倍数。
固定**测试端为 canonical 的 \(B\)**，先数带约化标记的同态，再忘掉该端同构。
这个端在特征零的自同构群恒为 \(\mathbf Z[i]^\times=\{\pm1,\pm i\}\)，
所以除数为 4。它既不是特殊纤维的 24 个自同构，也不是中间非极大 CM 阶的两个单位。
§5 处理后者在 Hecke 推前中的重数，不能再用它改动这个除数。

## 3. 奇度的细变形长度

采用 Gross 的局部变形计算：
[On canonical and quasi-canonical liftings](https://archive.mpim-bonn.mpg.de/id/eprint/3578/1/preprint_1985_30.pdf)，
该文件最后附录 §§3–5，尤其 Proposition 4.3。
这里只使用附录的局部命题，不套用主文假设奇判别式的整体交数公式。

令 \(K=\mathbf Q_2(i)\)，\(\pi=1+i\)，则 \(e=2,f=1\)。
Gross 的编号约定是：模 \(\pi^{m+1}\) 的端同态阶为
\({\cal O}_K+\pi^m{\cal H}\)。
若 \(\beta_-=(c+di)j/2\)，则
\(v_2N(\beta_-)=L(\beta)-2\)。
Proposition 4.3 的条件
\(v_2N(\beta_-)\ge1-e+mf\) 等价于 \(m+1\le L(\beta)\)。
故细变形空间的 \(\pi\)-长度为 \(L(\beta)\)，
按 \(v_2(2)=1\) 规范化后为 \(L(\beta)/2\)。

相关特殊项链点除去恒作用 \(\{\pm1\}\) 后，有效粗稳定子为 \(C_2\)。
粗 Cartier 方程的拉回是两个细局部分支因子的范数；
对上述相交，两因子的估值相等。因此粗长度为 \(L(\beta)\)。
与 §2 的四单位除数合并，非 Gaussian 项给 \(\frac14\sum Lw\)。
Cartier 方程的范数和测试端标记的忘却是两步不同操作。

## 4. 固定 \(j-1728\) 参数的自交

在特征 2，20 个 \([i]\)-固定项链按 \(t\leftrightarrow t^{-1}\)
两两具有相同粗约化点。非平方 \(t\) 不是 \(\pm1\)，故恰有 10 对。
每个相关粗点的有效稳定子为 \(C_2\)。

用 \(X_0(5)\) 的同一稳定子局部图计算积分参数：
共同的可表刚化模问题在两个 prime-to-2 层结构方向都为 étale，
取相同稳定子的商，得到对应粗完成局部环。
取 \(X_0(5)\) 参数
\[
 j=\frac{(t^2+10t+5)^3}{t},\qquad
 j-1728=\frac{(t^2+4t-1)^2(t^2+22t+125)}{t}. \tag{4}
\]
该恒等式可直接展开核实；公开公式见
[Elkies letter, equation (12)](https://magma.maths.usyd.edu.au/~watkins/papers/epz.pdf)。

两 canonical CM 截面为 \(t_\pm=-11\pm2i\)，均为单位，且
\[
 t_\pm^2+4t_\pm-1=-18(t_\pm+7),\quad
 v_2(t_\pm+7)=1,\quad 2t_\pm+22=\pm4i.
\]
所以
\[
 v_2\!\left(\frac{d(j-1728)}{dt}(t_\pm)\right)=2\cdot2+2=6. \tag{5}
\]
若 \(j-1728=a(t-t_\pm)+\cdots\)，切向自交换参项为 \(-v_2(a)\)；
20 个对角项总和为 \(-120\)。
另一方面 \(v_2(t_+-t_-)=v_2(4i)=2\)，
10 对中的两个有序交叉项各贡献 2，总和为 \(40\)。
因此
\[
 I_2(B,B)=-120+40=-80. \tag{6}
\]
尖点与 CM 支持不交；固定积分尖点参数的自交项为零。
2 处的好约化又使次数为零的 \(B\) 无需非平凡垂直修正。

对 \(n=1\)，非 Gaussian 的特殊纤维自同构仍贡献上述交叉 \(40\)，
不能将 return 整体删掉。一般奇 \(n\) 的 Gaussian return 也保留交叉项，
只另加每个 return 中 20 个真正对角项 \(-6\)，
所以修正恰为 \(-120\rho(n)\)。

## 5. 偶度：完整格分类、粗商和推前重数

写 \(n=2^kr\)，\(r\) 为奇数。固定奇度的一个带标记匹配，
再分解全部阶 \(2^k\) 子群。
令 \({\cal O}=\mathbf Z_2[i]\)、\({\cal O}_s=\mathbf Z_2+2^s{\cal O}\)。
指数 \(2^k\) 的 rank-two superlattice \(T'\supset{\cal O}\)
按其 multiplier order 唯一分为 \(0\le s\le k\) 的层，并写为
\[
 T'=\pi^{-(k+s)}u{\cal O}_s,\qquad
 u\in{\cal O}^{\times}/{\cal O}_s^{\times}. \tag{7}
\]
指数由 \([{\cal O}:{\cal O}_s]=2^s\) 得到；
包含条件等价于 \(k\ge s\)，因为 conductor 为
\(2^s{\cal O}=\pi^{2s}{\cal O}\)。
局部二次阶的格的 homothety 分类也可由一组最小估值基向量得到 (7)。

对 \(s\ge1\)，\([{\cal O}^{\times}:{\cal O}_s^{\times}]=2^s\)。
因此细标记核数
\(1+\sum_{s=1}^k2^s=2^{k+1}-1=\sigma_1(2^k)\)，没有额外核遗漏。
这正是所有子群的 \(T_{2^k}\)；循环对应另以线性关系处理。

Gross Proposition 5.3 给 quasi-level \(s\) 的定义环在 \(K\) 的最大
非分歧基上有分歧次数 \(2^s\)，formal modulus 为该环的 uniformizer。
任一 canonical 参数，包括经奇范数残余同态换标记后的嵌入，
赋值至少为 \(1/2\)，而 quasi 参数赋值为 \(1/(2\cdot2^s)\)。
严格较小的后者决定两参数差的赋值。
所以每个相关细接触都为 \(1/(2\cdot2^s)\)，不要求奇度同态与 \(i\) 交换。

粗商与重数须同时处理：

1. \(i\notin{\cal O}_s^\times\)，而 \(i^2=-1\in{\cal O}_s^\times\)，
   故 \(i\) 在 \(2^s\) 个细点上自由配对。
2. 粗 Cartier 方程拉回是这一对细分支因子的乘积，
   因而每个细标记点对应的粗接触为 \(2^{-s}\)。
3. 忘掉源端细标记后，每个粗轨道在原 Hecke 推前中保留重数 2。
   按 \(2^s\) 个细点相加，等于按 \(2^{s-1}\) 个粗点各乘 2；
   不能再额外除 2。

整层贡献为 \(2^s\cdot2^{-s}=1\)。测试端仍为 canonical \(B\)，
四单位除数保持不变。
式 (7) 中额外的 \(\pi\)-homothety 只置换 20 个 \([i]\)-固定项链。
若
\[
 A(r)=\frac14\sum_{N\beta=r}w(\beta)
\]
包括 Gaussian 元素，则
\[
 I_2(B,T_{2^kr}B)=I_2(B,T_rB)+kA(r). \tag{8}
\]
例：\(T_2P\) 的两个非 canonical 核被 \(i\) 交换，
对应同一粗 CM16 点，推前重数为 2，不是一个权重 1 的分支。

## 6. 化为闭式

左乘 \(1+i\) 给
\[
 (a,b,c,d)\longmapsto(a-b,a+b,c-d,c+d).
\]
这是范数 \(r\) 元素到范数 \(2r\) 元素的双射。
它对非 Gaussian 元素使 \(L\) 增加 1，保持 \(w\)，并保持 \(\rho\)。
在 (8) 中，非 Gaussian 新增长度被 (1) 的求和吸收，
Gaussian 的新增层质量恰为 \(20\rho(n)k\)，故得 (1)。

## 7. 实际执行与准确来源

程序 [verify_r193_two_adic_local_heights.mjs](../notes/verify_r193_two_adic_local_heights.mjs)：
SHA-256 `a4123f3696524e38bc9a824c7159002d73306ea87b05508987324d8f75722ae6`。

证书 [r193_two_adic_local_heights_certificate.json](../notes/r193_two_adic_local_heights_certificate.json)：
SHA-256 `1f38dac125dbb9fb5bcdcb490feb64754639b8d8d47937c8e51b672a72cfd698`。

R190 输入 SHA-256 为
`b2bdf1471fefc76dd6d05523af8929b66ef770b479534378c414b657d8420b54`。
本次真实 Node 执行通过全部断言：
54 行共 56,616 个 Hurwitz 元素（56,460 个非 Gaussian）逐一矩阵匹配；
55 度的 2-除闭包中 19 个相邻倍增对逐一核验完整双射。
这是有限算术核验范围，不替代 §§3–5 的证明。

从本课题目录运行：

```bash
node notes/verify_r193_two_adic_local_heights.mjs \
  --odd notes/r190_odd_local_heights_certificate.json.gz \
  --output /tmp/r193_two_adic_local_heights_certificate.json
```

偶度粗商与重数另由 serre_literature 独立核对；
其完整格分类与本证明 §5 一致。全局 Serre 一致性仍按 README 保持开放。

