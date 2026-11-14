# R195：41 处普通点的局部项与完整非 47 修正向量

日期：2026-11-13（台北）；未推送结果的第二次恢复版本。
输入为已推送 R190 奇素数证书和重建 R193 的 2 处证书。

## 1. 结论和规范

沿用 \(X=X_{\rm ns}^{+}(41)\)、\(B=Z_{-4}-D_{\rm cusp}\)。
两个有效除子均为次数 20；CM 切向参数固定为 \(j-1728\)，尖点固定为 \(q_{41}\)。
对 \((n,41)=1\)，令
\(\rho(n)=\frac14\#\{\alpha\in\mathbf Z[i]:N\alpha=n\}\)。
本题普通 Hecke 标签满足
\[
 \boxed{I_{41}(B,T_nB)=-40\rho(n).} \tag{1}
\]
特殊标签 \(C_4=T_4-T_1\) 按线性相减，右端为零。

结合 R190/R193，全部非 47 局部项为
\[
 K_n=K_{n,\mathrm{odd},\,\ell\ne41,47}
      +I_2(B,T_nB)\log_{47}(2)-40\rho(n)\log_{47}(41)
      \pmod{47^4}. \tag{2}
\]
其中 \(47^4=4\,879\,681\)，对数消去 Teichmüller 部分。

| 对应 | \(I_2\) | \(I_{41}\) | \(K_n\bmod47^4\) |
|---|---:|---:|---:|
| \(T_1\) | \(-80\) | \(-40\) | \(4\,226\,475\) |
| \(T_2\) | \(-40\) | \(-40\) | \(1\,840\,520\) |
| \(T_3\) | \(0\) | \(0\) | \(3\,638\,646\) |
| \(C_4\) | \(80\) | \(0\) | \(3\,837\,879\) |

全局高度方程为 \(h(B,S_iB)=\lambda_{47}(e_i)-K_i\)。
本条只确定完整局部修正向量，不将其余待算 \(\lambda_{47}\) 视为已知。

## 2. 在正确的半稳定模型上分离支持

Edixhoven–Parent，
[Semistable Reduction of Modular Curves Associated with Maximal Subgroups in Prime Level](https://websites.math.leidenuniv.nl/edixhoven/publications/2021/xpnonsplit_model_documenta.pdf)，
Theorems 3.3、3.5，提供模型输入：
最大非分歧基上作次数 \(e=(41^2-1)/2=840\) 的全分歧基变换后，
两个普通垂直分量均为 \(\operatorname{Ig}(41)/C_4\)，经超奇异分量连接。

下文的“不同约化点”均指这个模型，不能从未作基变换的原模型直接读交数。
因 \(41\equiv1\pmod4\)，\(j=1728\) 在特征 41 是普通点。
一个普通方向上的 Igusa 生成元由 \(\mathbf F_{41}^{\times}/C_4\) 标记，共 10 个。
在 \(j=1728\) 处，椭圆曲线的四单位已经包含在此 \(C_4\) 商中，
所以每个分量仍有 10 个不同粗 Igusa 点。
下节局部变形显示每一个都有唯一 \(w=1\) 的 \([i]\)-固定 CM 截面。
两分量的 20 个截面遂恰为全部 \(Z_{-4}\)。

尖点的 Igusa 生成元具有同样的商标记，20 个尖点也在两个分量各落 10 点，
并避开超奇异分量和节点。于是 \(B\) 对每个特殊纤维不可约分量的交数为零，
故垂直修正可取 \(\Phi_{41}(B)=0\)。
不必额外假定 \(T_nB\) 的每个有效部分有相同分布。
这只消去了图上的修正；固定切向参数的自交仍须计算。

## 3. 普通变形与粗参数的导数

先加可表辅助层结构，在细变形环工作。
普通 \(p\)-divisible group 是 étale 群和乘法群的扩张，
其 Serre–Tate 扩张参数记为 \(q_{\rm ST}\)，canonical lift 对应 \(q_{\rm ST}=1\)。

全 41 级标记使这个扩张在 41-torsion 上分裂。
在已含 \(\zeta_{41}\) 的基上，分裂参数 \(w\) 满足
\[
 q_{\rm ST}=w^{41}. \tag{3}
\]
这是扩张类在乘法形式群中的 41 次幂映射。
\([i]\) 在 connected 与 étale 两方向的特征相反，故作用为
\(w\mapsto w^{-1}\)。所考察的 CM 椭圆点被它固定，
而靠近 canonical lift 的固定解只有 \(w=1\)。

去掉恒作用的 \(\{\pm1\}\)，有效粗稳定子是 \(C_2\)。
因为 2 可逆，不变子环的积分参数可取
\[
 z=w+w^{-1}-2=(w-1)^2/w. \tag{4}
\]
底层椭圆曲线粗空间对应参数为
\(z_0=q_{\rm ST}+q_{\rm ST}^{-1}-2\)。
在普通 \(j=1728\) 点，
\(j-1728=u z_0+O(z_0^2)\)，\(u\) 为单位：
特征 41 大于 3，细椭圆曲线变形到 \(j\) 的分歧恰为这个二阶自同构商。

定义整数多项式
\[
 C_0(X)=2,\quad C_1(X)=X,\quad C_{m+1}(X)=XC_m(X)-C_{m-1}(X).
\]
它满足 \(C_m(w+w^{-1})=w^m+w^{-m}\)，所以
\(z_0=C_{41}(z+2)-2\)。
递推或在 \(w=1\) 展开给
\[
 C_{41}'(2)=41^2,\qquad
 j-1728=u\,41^2z+O(z^2). \tag{5}
\]
每个 CM 对角项的换参自交是
\(-v_{41}(u\,41^2)=-2\)，20 个点的 trace 自交为 \(-40\)。

只用细参数中的导数 41 会漏掉粗二阶商带来的第二个 41。
同时，规范化一直为 \(v_{41}(41)=1\)：
在分歧基上所得整数长度须除以基变换次数 840，
不能在最终公式再乘 840。

## 4. Gaussian return 与其他相交的排除

从 canonical ordinary \(E\) 出发的 prime-to-41 子群为 étale，
其商仍是约化商曲线的 canonical lift。
若商在特征 41 有 \(j=1728\)，canonical lift 的唯一性迫使特征零的
\(j\) 也为 1728。因此 isogeny 来自 \(\mathbf Z[i]\) 中范数 \(n\) 的元素，
模四单位后恰有 \(\rho(n)\) 个。

反之，每个 Gaussian isogeny 与 \(i\) 交换，置换全部 20 个固定项链。
在 R193 式 (2) 的矩阵标记中，对 \(\alpha=a+bi\) 该置换为
\[
 t\longmapsto
 \left(\frac{a+9b}{a-9b}\right)^2t. \tag{6}
\]
\(N\alpha=n\) 与 41 互素，分母非零，且它确为 20 个非平方标签的置换。
因此每个 Gaussian return 的有效除子都是 \(Z_{-4}\)，
各贡献 \(-40\)，即得 (1)。

其他 CM 商在本模型中与 \(Z_{-4}\) 不相交。
CM 点的 \(j\) 为积分有限值，尖点在 \(j=\infty\)，两类支持亦不交。
尖点参数 \(q_{41}\) 为积分坐标；prime-to-41 Hecke 的 Tate 指数和单位
在 41 处均为单位，同尖点的切向正则化没有额外 41 次幂。
不同尖点已在本模型上分离，所以没有遗漏的尖点项。

## 5. 完整向量的实际算术核验

对 \(47\nmid a\)，令 \(Z=a^{46}-1\pmod{47^4}\)，则
\[
 \log_{47}(a)=\frac1{46}\left(Z-\frac{Z^2}{2}+\frac{Z^3}{3}\right)
 \pmod{47^4}.
\]
第四项估值至少为 4，故可截断。真实程序得到
\[
 \log_{47}(2)=2\,363\,771,\qquad
 \log_{47}(41)=1\,315\,812.
\]
程序从 R190 读取全部 54 标签并与 R193 对齐，
独立枚举 Gaussian 范数元素，核对 return 数和 (6) 的实际置换；
整数展开 \(C_{41}(z+2)-2\)，核定线性系数 1681；
将每个素数的系数合并，再独立重算其对数和。

全向量保存在证书的 `rows`，含各素数系数、\(I_2,I_{41}\)、
Gaussian 置换与 \(K_i\)。它不使用浮点计算，也不代替 §§2–4 的几何证明。

程序 [verify_r195_level41_local_heights.mjs](../notes/verify_r195_level41_local_heights.mjs)：
SHA-256 `255d1cdcd83a0bc8cf82d5c9ea00a0df7a31f5e251b6161b0c7d44d98849d645`。

证书 [r195_non47_local_heights_certificate.json](../notes/r195_non47_local_heights_certificate.json)：
SHA-256 `5d77f52d05dcc5945c3bf9258de0252046ed6871850bcf6da17db2465a7eaad3`。

R190 输入 SHA-256：
`b2bdf1471fefc76dd6d05523af8929b66ef770b479534378c414b657d8420b54`；
R193 输入 SHA-256：
`1f38dac125dbb9fb5bcdcb490feb64754639b8d8d47937c8e51b672a72cfd698`。

从本课题目录运行：

```bash
node notes/verify_r195_level41_local_heights.mjs \
  --odd notes/r190_odd_local_heights_certificate.json.gz \
  --two notes/r193_two_adic_local_heights_certificate.json \
  --output /tmp/r195_non47_local_heights_certificate.json
```

第二次环境恢复后已真实 Node 执行，全部断言通过并写盘。
全局高度、完整 QC 根与绝对 Serre 一致性按各自尚缺输入继续推进。

