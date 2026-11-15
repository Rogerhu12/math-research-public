# R796：原 CM 点的144条全局二次关系已准确完成

2026-11-15，serre-public-astra-20261115。本文登记公开仓库自己的
[run 43693301389](https://github.com/Rogerhu12/math-research-public/actions/runs/43693301389)
实际结果。数学内容沿用
[R796原二次局部图证明](R796-original-CM-local-chart-from-quadratic-sections.md)，
原 $Y_K$、$P_1$、粗坐标 $z=a-1$ 和 R790 的 $82^2$ 尺度保持。

## 1. 实际选出的原局部图

原146条 M2 基中，实际选择
$\tau=s_0$ 为值锚点，第1行为切向锚点。
从原 R790 值和首粗导适配后，真实数据为

$$
\tau(P_1)=\frac{67419}{4},\qquad
\lambda=\frac{dt}{dz}(P_1)
=-\frac{36197717076}{172095737},\qquad t=\sigma/\tau.
$$

$\sigma$ 和144个 $u_j$ 的原基坐标、清分母尺度及逆变换都准确保存；
全部点值与首导条件均已代回。
**实际适配系数并不全在 $\mathbb Q$。**
本次因此使用真实的 $K=\mathbb Q(\zeta)$ 两分量，
把416阶 $K$ 方程实现为832阶有理方程，未采用不适用的纯有理捷径。

在 $W_{P_1}$ 的10585个有序二次候选中，
实际扫描7936个，选出416个独立乘积。
所用辅助素数为1000000009，$\zeta$ 分支为115381398；
真实416阶 minor 的行列式为823199261模该素数，非零。
这是新的短系数矩阵的实际 minor，未沿用旧较长模形式矩阵的 minor。

144个右端 $\tau u_j$ 的准确解具有一个1447位十进制公共分母。
核心随后在全部 $q_Y^0,\ldots,q_Y^{27}$、40个 $\xi$ 坐标和两个 $K$ 分量上
检查整数清分母残差，全部为零。
由 $20\cdot28=560>544=\deg(2\mathcal L)$，
这些是原曲线上的144条全局恒等式。

## 2. 已完成的局部长度及直接用途

在 $\tau\ne0$ 的图中，这些真实关系给

$$
x_j=Q_j(t,x_1,\ldots,x_{144}),\qquad x_j=u_j/\tau,
$$

其中每个 $Q_j$ 为保存下来的二次式。
原点处关于 $x$ 的隐函数 Jacobian 为 $I_{144}$。
结合真实非零 $\lambda$，这是原曲线的唯一形式局部分支，
不是另行选择的代数根。

本次请求长度为2，实际也只完成长度2：
输出全部原 $s_i/\tau$ 的常数和一次系数，
并验证其回到原 $z$ 方向后恰为 R790 的值和首导。
没有生成二次以上的局部展开，也没有计算原函数 $A/B$、$\beta$、$\eta$ 或高度。

后继需要更高长度时，沿同一冻结关系按 R796 的递推只增加新阶。
原普通三、五、六次幂的局部值由既有 product recipe 接合；
不重算E1、原M2 cusp前缀、CM挠点变形或原Laurent。
实际胖点核和函数共同零分支仍须由各消费者输出自己的准确证书。

## 3. 不可变来源和真实执行

源提交：`4ed3a5bf4298f930e018527ddea4c940d936236c`。
公开 job：`132748285798`，2026-11-15 08:11:05–08:14:16 UTC。
数学核心实际用时165.797146337秒。
执行为本公开仓库 GitHub Actions、Python 3.12、python-flint 0.9.0。

| 对象 | SHA256 |
|---|---|
| 数学核心 | `636cf73825ff99b11b44c7186fd4ef5af9dcbb311949cdd0c03e08ea424218c6` |
| R796证明 | `8bf2662434d8117be5514cfbe9ba19fa089167c6e7bab76c079daded66fe40d4` |
| R796方法 | `2f9c5252eaf36f25fb87107ec938a5abd195faa287872be9773bea4ee955d706` |
| R793证明 | `6f716b64432227244a46d91f01ae2f46ba6d4a5f893666693ed07dec9e2e5cab` |
| 公开wrapper | `a711a2122cf220664b3903810184f429ff8e7dd43121a7d2b9752ff9ffc2b1e1` |
| 实际请求 | `7a4507fa013a03f5897a0baf2e8e5fe7133d437cec1d37b1728900b04a99192f` |
| workflow | `f59e8e1814f3d8976706dd6191c3a090e64dca0180b76db429968391a4965a05` |

只读取 R786 run43682100611 的原146条M2前缀与
R790 run43688215703 的原146条CM值/首导。
各组来源、148个消费文件以及全部原metadata的绑定见
`notes/R796-public-original-CM-quadratic-chart-request.json`。
两组的原 M2 recipe SHA 完全相同，146个原索引/recipe/尺度逐项对齐。

## 4. 实际输出绑定

| 输出 | 大小或数量 | SHA256 |
|---|---:|---|
| 临时ZIP，artifact14153327234 | 124396609 B | `78d9e7ab8014add0f85c0b7b95ff1823d8308bed752e7ecbccc552005fb33ecc` |
| 完整输出manifest | 97530 B；558文件 | `7501f726dc6c5a5d8a4be498651ab55846fe6b0b73af7339ae8f6f41bde1f63c` |
| 完成证书 | 33514 B | `1b72c55b5bb9fc110d1630da16cf36ae5c1a8bf3e7783522a2c01167ad3835f0` |
| 原CM基适配 | 26113 B | `11a0989b79fb3b80e49b7dc1bbbc85ba26df006f9b43255a20275c6682d13a5a` |
| 真实416单项式及minor | 17085 B | `3025b17c93822fa0ece788ccbd416733af7d4fc5f73c18e63131ac4c85e4587c` |
| 完整准确全局关系 | 53320950 B | `b9f6ff45e84e1bd8b48b905153340bc09f127a0decdb29352d2de20829429aa6` |
| 长度2原比值jets | 19046 B | `50cab09598b8a3e2290ebbd6407016740722bef4eb8dbabc99ff5d70760ee849` |
| 阶段manifest | 42137 B；548阶段 | `da243d5dfd49a3acebd27f8f5bb1a3a6d328a47b6feb40adfc6c88fca14b3956` |
| 原输入活跃包 | 2322706 B | `982bf351de1bf0d3d8adfce109b9badc1877f0f250ea0bd2eee834279a6a2f68` |

临时artifact名为
`serre-global-R796-original-CM-quadratic-chart-43693301389-1`，
到期时间2026-11-16 08:14:06 UTC。
全局关系文件为`R796-original-global-quadratic-relations.json.gz`；
完成证书为`p41-original-CM-quadratic-chart-certificate.json`。

root 已核ZIP、全部558输出文件的大小和SHA、
全部548阶段的来源配置，以及实际wrapper的完整IO验证。
原run/source/core/proof/请求链均准确一致。
本地只进行文件、schema和哈希核验，没有执行数学核心。
来源小回执及文件SHA清单保于
`computations/R796-original-CM-quadratic-chart/43693301389-1/`；
完整矩阵、曲线关系、jets和可重算证书不入Git或Release。

本次已经得到后继可直接消费的原全局二次图；
原$\beta$、Jacobian中的$\eta$、规范高度和全$p$统一排除仍须继续完成。
