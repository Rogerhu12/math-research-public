# R150 补篇：两个原三次数域的低投影谱 $(3,3)$ 与全部六共轭点的目标局部来源

日期：2026-11-15 UTC。作者：Astra-ISP-789f / literature_audit。AI 辅助：GPT-6 Astra Pro。

状态：使用原十七式、次数不超过三的全部 $6188$ 个来源、原 $4367$ 个输出。两个三次数域均已完成精确运算及原来源校验。新结论是原九个 $h_0t_j$ 在 $F_+$ 和 $F_-$ 的全部根处都有局部来源；没有把低投影的完整谱冒充整个原矩阵的谱，也没有据此宣布全局多项式来源。

## 1. 原因子、目标及局部结论

沿用
$$
\begin{aligned}
F_+(s)&=5s^3-25s^2+32s-8,\\
F_-(s)&=5s^3+135s^2+864s+864,\\
E_8(s)&=5s^8+50s^7+153s^6-936s^5-2888s^4
       +15936s^3-3392s^2-25472s+9600,
\end{aligned}
$$
以及
$$
h_0=s^3(s-2)F_+^2F_-^2E_8.
$$
原九个目标准确为
$$
t_j(s,m)=\left(\sum_{a=0}^{j}\binom ja(-s)^{j-a}m_a\right)^2,
\qquad 2\le j\le10.
\tag{1.1}
$$
在完整二项式共动坐标中，它们是 $z_j^2$。原方程 primitive 行与固定 $\det J_3$ 倍原式之间仅差已付的非零有理常数；这里没有重标原目标。

令 $F=F_+$ 或 $F_-$，$R=\mathbb Q[s]_{(F)}$，
$$
A:R^{6188}\longrightarrow V=R^{4367},\quad L=\operatorname{im}A,\quad
W=(z_2,\ldots,z_{10})^2_{\le5}\subset V.
$$
$\operatorname{rank}W=4212$。本篇证明
$$
\boxed{6\le\delta_P\le\delta_A\le8,\qquad
       \ell_R\bigl(W/(L\cap W)\bigr)\le2,}
\tag{1.2}
$$
其中 $P$ 为真实原投影来源矩阵，$\delta$ 是局部有限扭子长度。因此
$$
\boxed{F^2W\subset L,\qquad h_0t_j\in L\quad(2\le j\le10).}
\tag{1.3}
$$
两因子在 $\mathbb Q$ 上不可约，故分别覆盖三个共轭点，合计全部六个复根。

所用不可约性、原完整常秩 $4352$、投影常秩 $140$ 分别见
[P+ 完整分类](R150-appendix-rank-one-Pplus-means-complete-critical-classification.md)、
[P− 完整分类](R150-appendix-rank-one-Pminus-means-complete-critical-classification.md)；
低支撑与完整投影的原式关系见
[非接触中心算子与原投影](R150-appendix-rank-one-noncontact-centered-rank-controls-macaulay-projection.md)。
原泛秩 $4354$、$W\subset L\otimes_R\operatorname{Frac}R$ 及投影泛秩 $142$ 见
[完整泛参数分类](R150-appendix-rank-one-mean-generic-complete-critical-classification-and-finite-exception-set.md)。

## 2. 低矩阵嵌入全部原投影来源

置 $c=z_0,d=z_1$。完整投影输出为
$$
c^a d^b,\quad1\le a+b\le5;\qquad
z_jc^a d^b,\quad2\le j\le10,\quad a+b\le4,
$$
共 $155$ 列。原十七式乘纯切向次数不超过三的十个单项式给出 $170$ 行；另有真实的 $54$ 个
$$
g(s)\,z_jd^2c^a d^b,\qquad
g=-2s^2(s-2)(s+6),\quad a+b\le2.
\tag{2.1}
$$
这 $54$ 行保留了 $g$。其与原一次横向乘子来源的互相生成由原纯系数 $g\eta_i$ 及某一真实 $\eta_i$ 局部为单位支付。本次逐多项式系数核了全部 $918$ 个一次横向来源，并按次数保留其余 $5100$ 个来源的零投影，合计全部 $6188$ 个原来源。

低矩阵 $S$ 取原十七式乘 $1,c,d$ 的 $51$ 行，以及
$$
c^a d^b,\quad1\le a+b\le3;\qquad
z_j,\ cz_j,\ dz_j,\quad2\le j\le10,
\tag{2.2}
$$
共 $36$ 列。这些列按原坐标零扩展进入 $155$ 列。所有未选高纯乘子行在这 $36$ 列上恒为零；全部 $54$ 个真实 $g$ 倍行也在其上恒为零。另有四个支撑不交的精确原核坐标
$$
c^4,\quad c^5,\quad c^3d,\quad c^4d.
\tag{2.3}
$$
这些是关于 $s$ 的多项式恒等式，已核全部 $0,\ldots,25$ 次系数，没有只核某个数域点后假设后续 Taylor 项。

故对每个 $N\ge1$，任一局部系数域 $K$ 上均有单射
$$
\boxed{\ker(S\bmod t^N)\ \oplus\ (K[t]/t^N)^4
\ \hookrightarrow\ \ker(P\bmod t^N).}
\tag{2.4}
$$
左侧第一项按低支撑零扩展，第二项取 (2.3)，支撑不交给出单射。这不要求完整投影的所有校正都具有低支撑。

## 3. 真三次数域、自然参数与精确小谱

取
$$
K=\mathbb Q[\alpha]/(F(\alpha)),\qquad t=s-\alpha.
$$
实际 companion 核了 $F(\alpha)=0$、$F'(\alpha)\ne0$，因此 $F(s)$ 与自然参数 $t$ 在 $K[[t]]$ 中相差单位。$g(\alpha)$、用于恢复来源的原纯系数，以及 $h_0/F^2$ 均实际核为非零数域单位。

原系数直接由原 $K,J_2,J_3$ 和全部中心式重建，不用参数插值，也不在专门点先除 primitive 内容。$51\times36$ 数域矩阵的 Taylor 系数经正则表示变成 $153\times108$ 有理矩阵，每个乘法块均核为同一数域元素的实际乘法。

两个域的实际单位 Schur 退出秩相同：

| 退出阶 $e$ | 有理正则表示退出秩 | 数域退出秩 | 累计数域秩 |
|---:|---:|---:|---:|
| $0$ | $75$ | $25$ | $25$ |
| $1$ | $0$ | $0$ | $25$ |
| $2$ | $0$ | $0$ | $25$ |
| $3$ | $6$ | $2$ | $27$ |

每一非零阶段仅解实际单位块右端，核全部 Taylor 卷积和完整剩余 Schur，不构造全逆。到 $e=3$ 已达到小矩阵泛秩 $27$，余下实际截断系数全部为零。因此小矩阵在每个域的非零 Smith 谱为
$$
\boxed{0^{25},3,3,}
$$
另有九个自由核方向，并且
$$
\boxed{\delta_S=6.}
\tag{3.1}
$$
长度取在 $K[[t]]$ 上。正则表示把每个数域方向展开为三个有理方向，因而有理展开的长度为 $18$；除以域次数 $3$ 才是 (3.1) 的局部长度 $6$。

## 4. 从低谱到完整投影长度

对泛秩 $r$、有 $n$ 列的矩阵 $M$，模 $t^N$ 右核维数为
$$
\dim_K\ker(M\bmod t^N)
=(n-r)N+\sum_i\min(a_i,N),
\tag{4.1}
$$
其中 $a_i>0$ 为正 Smith 指数。

(3.1) 给出低矩阵右核维数 $9N+2\min(3,N)$。完整投影有 $155$ 列、泛秩 $142$，自由项为 $13N$。代入真实单射 (2.4) 后，自由项 $9N+4N=13N$ 恰好抵消，得到
$$
\sum_i\min(a_i(P),N)\ge2\min(3,N).
$$
取 $N=3$ 即推出
$$
\boxed{\delta_P\ge6.}
\tag{4.2}
$$
无须把低矩阵核说成完整投影核，也无须假设高支撑校正为零。

原整数整块的模 $31$ 完整最大子式因子给每个不可约 $F_\pm$ 的特征零长度上界
$$
\delta_A\le8.
\tag{4.3}
$$
原行单位及模素数因子区分见
[完整仿射扭子因子](R150-appendix-complete-mod31-torsion-and-affine-maximal-minor-divisor.md)
与[原局部投影差长准则](R150-appendix-original-local-projection-length-gap-and-two-point-length-bound30.md)。
(4.2)、(4.3) 分别是下界、上界，本篇没有计算 $\delta_P$ 或 $\delta_A$ 的精确值。

## 5. 真实九目标的局部来源

原泛型像包含 $W$，故 $T=W/(L\cap W)$ 是有限扭子模。环境商给精确序列
$$
0\longrightarrow T\longrightarrow V/L
\longrightarrow(V/W)/\pi L\longrightarrow0.
\tag{5.1}
$$
取有限扭子仍精确：右端扭子类的任意提升经某个 $t$ 幂落入 $T$，再乘 $T$ 的消去幂即为扭子。于是
$$
\ell_R(T)=\delta_A-\delta_P\le8-6=2.
$$
长度不超过二的离散赋值环扭子模被均匀化参数平方消去，故 $F^2W\subset L$。本次实际核了 $h_0/F^2$ 是数域单位，再结合原目标身份 (1.1)，即得全部九个 $h_0t_j$ 的局部来源。

数域完成是忠实平坦的，因此 $K[[t]]$ 中的成员关系下降到 $\mathbb Q[s]_{(F)}$。来源始终为原十七式乘次数不超过三的多项式，局部化仅允许参数分母在该因子处为单位。

当前付的是 $F^2W$，没有断言 $W$ 自身已在局部像中。两个因子处的结论也不单独推出全局 $\mathbb Q[s]$ 来源。

## 6. 实际执行与可复算证据

[完整同源代码](../notes/2026-11-15-r150-cubic-original-low-projection-local-smith-789f.py)
长 $22142$ 字节，SHA256 为
4956f0dc77aa9d16f064e65c4c803625fb221cd81c7f067aeb265c3bd96f07fd。

参数为 --point plus/minus，--max-order 4，--remaining-seconds 90，--memory-mib 1024；原重建器及 Schur helper 的完整 SHA 固定在源码和回执中。

实际 run 为 43731613530：

| 因子 | execution source | 数学秒数 | 原小回执字节 | 原小回执 SHA256 |
|---|---|---:|---:|---|
| $F_+$ | 94c955b8f7221a5dc51a378a37d9f2057fe68ecf | $9.738919457000009$ | $15732$ | 19c6a404c77dd26afb59da72fbe7219c477c8a7e86602f725030bf887f0ddd4b |
| $F_-$ | 78b3a92e16a6b75ec154997e03f9c8b7577bc177 | $10.51091103200001$ | $15793$ | 06db12970af9b8f791f734e113b87d4ccf18947fab17fa6384dcac37ade670ba |

两项退出码均为 $0$。仓库小回执为
[F+ 实际记录](../notes/r150-local-projection-session-789f/43731613530-cubic-plus-original-low-projection-order4.json)
与 [F− 实际记录](../notes/r150-local-projection-session-789f/43731613530-cubic-minus-original-low-projection-order4.json)。
它们保存全部原多项式、数域乘法块、每阶单位解及完整 Schur 的身份哈希；未上传可重算大矩阵或旧正常形。本篇使用这两次成功发布的执行，不将此前发布目录错误中止的 job 计作独立新增数学。

## 7. 公共最大子式因子与条件费用

本篇使两个三次因子在原全部最大子式中的公共指数各从 $2$ 提高到至少 $6$。结合已经证明的零点长度 $66$、负六点长度 $12$、二点常秩所给下界 $9$ 及 $E_8$ 下界 $2$，可取
$$
K_{139}=s^{66}(s-2)^9(s+6)^{12}F_+^6F_-^6E_8^2,\qquad
\deg K_{139}=139.
$$
其首项为 $5^{14}$，仍是 $31$ 单位。这里使用的是原全部最大子式的公共因子，不是较小阶子式的因子。

沿[负六补篇第七节](R150-appendix-minus-six-local-smith-length12-and-original-nine-target-membership.md)的同一选定子式、权和 $8770$、无穷远界 $130/125/125$，有
$$
8527\le\deg D\le8640,\qquad
8388\le q:=\deg(D/K_{139})\le8501.
$$
三支费用变为
$$
\begin{aligned}
\text{非基来源}&\le8501-1+45=8545,\\
\text{原来源转移}&\le8770+55-125-139-11=8550,\\
\text{目标伴随支路}&\le8770+64-125-139-10-8388=172.
\end{aligned}
$$
因此九个原目标若已属于全局 $\mathbb Q[s]$ 原来源像，可取统一费用至多 $8550$。本篇只关闭两个三次因子处的局部条件，未支付全局成员性，也未支付固定 $D$ 首项的 $31$ 单位条件。
