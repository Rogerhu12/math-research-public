# R133 实算：精确 bump 包络与完整连续 $Z$ 的已知源

2026-11-14。公开 run [43610523058](https://github.com/Rogerhu12/math-research-public/actions/runs/43610523058)
已真实成功，数学 child 返回 0，10 个门全部通过。producer 耗时
76.875693837 秒，child 实际 wall 85.002589378 秒。新 target 调用为
**0**；原 80 次 fixed-$\eta_0$ 调用及对应保存的 jets 全部复用。

这是 14 个原格及其中 40 个已存在子格上的新严格源包络。
它不宣称 7721 格新方法全覆盖，不宣称完整 PDE 响应或无限维 inverse。

## 1. 精确证据身份

目录为
`notes/exact_bump_Z_source_ci/run-43610523058-1-exact-bump-and-continuous-Z-source-pilot/`。

| 原件 | SHA256 |
|---|---|
| 完整 native | `c37a5796a3829dfab1846928041f6a91472dc47f20e02f8a2a4080198b574b1c` |
| 本次已读 repo process | `49e19cfbc099e3330c047438f95f70a17eb5ae70f60d026988a5aa3038d227db` |
| 完整 summary | `9b07a2144f3492558de17530971d1141733fb1cb97876aa69748488fba15f853` |
| 新数学 producer | `2d45c2f100484f5a25fe50ec2d8ea2dcd601b79f1f151d4be116225d3284fcc8` |
| 新 manifest | `563fc148bf219581259eea090271c37f4760115cc6d09e40c0437a14ee93b7bd` |

native 逻辑文件为
`native/exact-bump-and-continuous-Z-source-pilot.json.gz`，
11802184 bytes，repo 以 6 个原字节片保存，完整原件保留在 Actions artifact。
summary 为
`evidence/exact-bump-and-continuous-Z-source-pilot-summary.json`。
该原件实际为 105167 bytes，超过集成传输文件限制，保持原件不删改；
后续只能在公开 Actions 中读取，或由新消费者导出小于 60 KB 的精简文本，
不再通过集成搬运这份完整 summary。
process 的 SHA 明确指本次已读 repo snapshot，不能冒称下载 artifact
内可能多记录一次 publication checkpoint 的同名过程字节。

旧 fixed-jet native 仍为 `a73382575ca2b14afb810c2ed43ae0aec9d59aef563635a19f6785b414111993`；
本次实际消费其 artifact process SHA
`479a4f2b39fccb834c8301e023c2260722bee923ee1755c8c4ac14fee6de4310`。
原 131 个 manifest 文件全部原 SHA 保留，新闭合共 136 文件。

## 2. 已解决的包络问题

原 compact bump 仍准确为 $w=4096[t(1-t)]^6$，支集仍为
$[1/20,9/50]$。新实现先在有理数域展开局部系数，再交原有向
`RadialFourier.scalar`，逐系数核对 $h^{-1}\partial_xw=w_r$，
并保留每个 Arb 与 binary64 coefficient radius。原完整 $F_\nu$
公式和 angular 支撑没有改变。

旧范数运算分别包围 $t$ 和 $1-t$ 再乘方，丢失系数抵消。新实现
消除这个额外放大，同时复用所有 intrinsic target/primitive 费用。
没有更换候选、方向、mean ODE 或背景。

同一已补 mean 的 $q_*$，原格 1524 的旧完整非均值 $160$ 输出
上界约 $0.0383623231$；新 exact-bump low193 上界为

$$
\|P_{\le96}R(q_*)\|_{L^2_\varphi}<5.336857\,10^{-6}.
$$

该比较的输出投影范围明确不同，完整 high 行仍另列。新源的改进
不能被理解为丢弃 high，或者把 $q_*$ 宣称为真正响应。

## 3. 连续 $Z$ 的完整 mean 被保留

相位线使用的 $Z$ 是原 full193 trial 的准确连续修补，其定义 SHA 为
`6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04`。
它与 $q_*$ 分开处理。

新 $Z$ 残差从 raw trial 的两条完整行开始，保留第二条真正 mean。
原片内 $Z-q_{\rm raw}$ 径向常值，故追加完整 operator offset 费
$a_0E_0+a_1E_1$；再追加已完成背景修补源和
$M_0E_0+M_1E_1$。上述费用保 principal、reaction、primitive、
mean rank，不能把 mean residual 设置为零。

以下均为同一连续修补背景、固定物理 $\eta_0,\nu$ 上完整 low193
普通圈 $L^2$ 残差的严格上界：

| 原格 | 原全参数 jets 的新界 | 复用已成 4 子格后的界 |
|---|---:|---:|
| 0，腰端邻域 | $4.309905\,10^{-7}$ | 未请求 |
| 1280 | $2.910112\,10^{-6}$ | $3.412986\,10^{-7}$ |
| 1289 | $3.846025\,10^{-6}$ | $6.170111\,10^{-7}$ |
| 1519 | $7.842382\,10^{-7}$ | $2.688866\,10^{-7}$ |
| 1524 | $9.628404\,10^{-7}$ | $2.957838\,10^{-7}$ |
| 6375，cut 左迹所属格 | $7.095042\,10^{-8}$ | $7.039040\,10^{-8}$ |

表中界包含完整 $Z$ mean 和真实背景修补费用；每个子格族严格覆盖
对应原格。所有 full-through160 与 high97-through160 界也保存在
native 中，未授给未知 high 解算子。

## 4. 后续全覆盖的准确接线

旧原 40 parts 已保存完整 raw 非均值残差与 signed mean residual。
可利用 mean 的 $L^2$ 正交性，为所有其余原格构造完整 raw 两行界，
再追加同一 $Z$ 修补费用；compact 支集内尚未采用新方法的原格
另行分派，已成 14 格及 40 子格不重算。

最终源覆盖必须与同一 $Z$ 的腰/cut 真迹相接，再消费原有向
continuous Green ports。$q_*$ 的边界源不能直接改名为 $Z$；
未知 high 反馈、整个 BVP 与相位响应误差仍须独立支付。
