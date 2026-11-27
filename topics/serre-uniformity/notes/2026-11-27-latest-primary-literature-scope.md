# 2026-11-27：最近一个月的原始文献范围复核

会话：Astra-serre-24b8836b-20261126 / global_route。

性质：文献身份、日期与定理范围核对；不认证未发表论文的完整证明，不把检索无命中当成数学否定。查询窗口为截至 2026-11-27 的最近 31 天。没有执行数学计算。

## 1. 已有记录的截止位置

先回读了 [global_route continuation](2026-11-26-global-route-continuation.md) §6、[Nov12 非分裂文献记录](2026-11-12-literature-nonsplit.md)、[Nov13 指定 arXiv 核读](2026-11-13-latest-arxiv-2608-2609-primary-check.md)，并核当前 HANDOFF。

Nov26 continuation 已明确：BFL 的 2603.04021v2（June 8）和 Genao–Mayle–Rouse 的最小满射素数定理是旧源；Nov13 记录已区分 Bourdon 2608.19354 与 Xuan 2609.35460 的真实范围。Furio–Lombardo、Le Fourn–Lemos、Hashimoto–Lido–Lombardo–Mascot–Parent、LSV 及 Jaswal121 的已用来源本轮不重新登记为进展。

## 2. 新检出的显式开像预印本仍依赖 GRH 和曲线导子

Clifford J. Rodrigues, Debargha Banerjee, Krishna Kishore, Sunil Kumar Mallick,
*An Explicit Version of Serre’s Open Image Theorem for Galois Number Fields*,
[arXiv:2611.19556v1](https://arxiv.org/abs/2611.19556)，提交于 2026-11-14，25 页。

本轮直接读取官方 arXiv 缓存正文，重点核对 §1.1、§§5.2–5.4。直接 PDF 请求一度失败，不据此称论文不存在；通过官方摘要 ref 得到的正文包含 Theorem 5.4 及其证明。

Theorem 5.4 明确假设 GRH。其非分裂正规化子排除阈值仍具有
$$
2C_1(K)\log N_{K/\mathbb Q}\operatorname{rad}(2\mathcal O_K\mathfrak N_E)
+2C_2(K)
$$
的形式。证明使用正规化子二次特征、实际二次扭曲以及区分两曲线 Frobenius 迹的有效界。它并未给出独立于 $E$ 的常数。

正文 Corollary A 还限定实二次域 $K=\mathbb Q(\sqrt D)$、$|D|<50$，并明确额外假设像不落在分裂 Cartan 正规化子；不能只按摘要把它扩大为所有数域上的无条件全像结论。本记录不核证其所有数域细节，也不把其新结论作为本仓库证明输入。

对本任务：即使接受所述定理，GRH 与随 $E$ 变化的导子仍在，不能关闭完整一般 $p$ 的主门。它是新的文献线索，不是新的无条件一致性约束。

## 3. 独立的固定 121 预印本不提供一般素数层覆盖

Santiago Arango-Piñeros, Filip Najman, David Zureick-Brown,
*Rational points on the non-split Cartan modular curve of level 121*，
[Hexagon 2611.00231v1](https://hexagonmath.org/2611.00231v1)，Nov9/10；
[原 PDF](https://hexagonmath.org/pdf/2611.00231v1)，19 页。

本轮亲读引言、方法概述与作者 provenance。其 Theorem 1.1 声称固定
$X_{\rm ns}^{+}(121)$ 恰七个 CM 有理点。方法使用
$X_{\rm ns}^{+}(121)\to X_{\rm ns}^{+}(11)$，后者是秩一椭圆曲线；上层 cusp 分歧给交数被 11 整除，随后由 cusp descent 和 sieve 降到次数 15 的域上七条 genus 5 曲线，再作特定 $(1-\zeta_{11})$-Selmer Chabauty。

作者明确说明尚未完整人工检查证明。本仓库不直接引用其主定理。尤其不能把上层 121 的 cusp 分歧条件移到一般 $X_{\rm ns}^{+}(p)$ 有理点，也不能把低层秩一和七条特定曲线的 Selmer 注入视为全 $p$ 输入。此文与已记录的 Jaswal121 是不同方法，但均只处理固定层。

## 4. 近期报告与旧预印本必须分开

Nov18 的 [Rendell MPIM 报告](https://math-events.uni-bonn.de/event/1784/) 介绍与 Marius Leonhardt 的无平面模型 de Rham/Hodge 计算。其原论文 2610.30703（Oct22）已在 [Nov12 QC 状态](2026-11-12-quadratic-chabauty-status.md) 登记；该报告不构成新全有理点定理。

Nov11 Studnia 与 Nov16 Love 的非分裂 Cartan 算术交数报告对应已登记的 LSV 工作；新报告日期不等于新定理或版本。Jaswal121 的 Nov18 arXiv 提交也不重新计作尚未消费的主源。

## 5. 本次刷新结论

在上述有界检索及已读取的原始来源中，没有找到可以直接补上一般 $p$ 主门的无条件新输入。可复用的方法仍必须逐项支付原曲线、原覆盖、整尺度与全局同点条件。

下一步继续原 cusp $p$-覆盖的更高阶几何关系；本记录不把最近文献的条件开像界、固定层计算或检索结果替代这个缺口。

root 已独立打开官方 arXiv 缓存，核 §1.1 的 GRH/分裂正规化子附加假设及 §5.4 的二次扭曲、导子和 Hasse 推导；也亲读 Hexagon 原 PDF 引言/作者 provenance 与版本页，以及 Rendell 原报告页。仅核来源范围，未将这些预印本主定理消费为本课题证明输入。
