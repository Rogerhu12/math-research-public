# 静态 W4：只读已付原根的一次完整自然通量观察

日期：2026-11-16。状态：新入口和本设计仅静态编写，未执行人工或研究。只有根代理统一公开 Actions 可以执行本入口。无新增完整 pure、self、秩、profile 数值、旧 forcing 或势函数生产。

## 1. 唯一数学目标

R417 已把整个静态真权负四自然像缩成
$$
\mathcal N(V_4(k))=(1+k^2)^3\{\mathcal N(V_4(0))+k^2\mathcal N(W_4)\},
\quad W_4=[h^{-4}k^8\omega^0(\log h)^0]F_0.
$$
其唯一剩余静态锚为 $a(1)$。本次只求完整 $\mathcal N(W_4)$，不把其非零先当正字符或 actual 联合像。

旧 R210 已在同一原 Gamma 规范付清该系数的 universal pure 响应坐标。原 R139 的全部两模式响应 DAG 也已保存。定义真实原成员
$$
\widehat W_4=W_4-\frac1{512}
(4R_0+8R_1-24R_2-R_3+36R_8+4R_9-17R_{12}+R_{15}-5R_{17}).
$$
这里下标全部是 **R139 的原列编号**。因为 $\pi\widehat W_4=0$，又完整自然 $\mathcal N$ 杀这些真实响应，
$$
\mathcal N(W_4)=\Omega(\widehat W_4)
=-4\int u'''M_{-2}^{\widehat W_4}(u,u).
$$
势 $N_0$ 已在保存的静态 $L_0$ 原根中。本幂无 $\Gamma$ 是 R417§3 的原系数结论；不是把未算的引用项置零。

## 2. 旧 pure 付款收据：只消费，不重做

- run 43688302217，job 132733352458；
- source 1b032593b46210e7a0599a224d5c2110fe1d1606；
- lane complete_pure_minus4_projection；
- 原 log：127473 B，SHA256 0cdf6ffa15b97cf926dad70b869945a782ee153dac317ec080d1b9d15c9030d6；
- 元数据收据 notes/actions-43688302217-1-complete_pure_minus4_projection/receipt.json：
  47378 B，SHA256 f739e4a0ccdcf5ea102a9deb5794486b8f9f022975764e23fd14b16ec6d722c4；
- 旧科学结果 complete-pure-minus4-result.json：
  53292 B，SHA256 aeea36d3c46f934ec784460367813ef7902f85f1c3492e575152fd6906e7a76a。
  原 payload 未保存在 Git；本入口不重建它。

运行时原 job API 必须仍为同 run/source 且 success，完整 log 字节/hash 必须一致。按原时间前缀剥除后的下列 **完整行含 LF** 精确选择：

| 原行 | 字节 | SHA256 |
|---|---:|---|
| MATHEMATICAL_RESULT | 924 | c21550ca39e7decce115eeef63bb661df7de2a9c601a27599a75d60152716880 |
| MATHEMATICAL_COLUMN global 44 | 346 | e4982bcf35410059ff9633a3916d9aade4bb36086a91484cd66ad19b77571b43 |
| 科学 EXECUTION_STATUS | 373 | f91f9abb0b2761c7c82c8b7d46138313d968250801771717f2bc4b23e8e83566 |

global44 的唯一原 alias 是 [0,[-4,8,0,0],"1/512"]。归一 pure SHA
25bd3f9cf5823f1e45b55eb344fdd10c818756e4e9f97192a91484c47ccfed59。
其 global 原列坐标为
[(0,4),(1,8),(2,-24),(3,-1),(8,36),(9,4),(12,-17),(14,1),(16,-5)]。
按旧四十保留列顺序，最后两个 global 下标对应 R139 原列 15 和 17。归一列必须乘 $1/512$，不能遗漏或重复此因子。新脚本逐项比较这一已有记录，不运行任何 pure 映射。

旧 log 同时含人工与科学的状态行；必须按精确行字节/hash 选择，不能要求所有状态 tag 只出现一次。

## 3. 唯一静态 mixed 原根

既有目录 notes/actions-43645177423-1-local_fourth_quotient：

- 原 run 43645177423，source 2f1b809c0b0abb7a26303d36940edc203815f872；
- local-fourth-quotient-original-expressions.json.gz：
  657195 B，SHA256 ea8ba97319ef3fa43ff8cacc7f98b106b13280aef4641b969f5f820194aebace；
- 解压原 JSON：3518194 B，
  SHA256 d74e87790a00a246e01438c54575c3190389e3adbdefed0cec233b6ec9a664d1。

使用冻结 head.bind_input("static",...) 的原 main/receipt/source/导出校验。
完整 metadata 应有 197 个 pure 和 197 个 mixed 状态，但只解码
mode=-2、指数状态 [-4,8,0,0] 的一个原 root，再做一次真权 $-4$ 的必要输入投影。其余原根不解码；不读取 pure root 以重验旧结论。

## 4. 九个 mixed 响应全部直接读既有 DAG

既有目录 notes/actions-43654534244-1-g_translation_successor：

- run 43654534244；
- source 1177f251dc3d9455adf88b585e4c0e4bd6f7e69b；
- main G-fifth-translation.json：24966 B，
  SHA256 faf6c2a0019ce614bb8d6f28b049f0a38a6c2f6e2e00930a1beab17e6c86f93e；
- receipt：34625 B，
  SHA256 e8f37f37ba85f822e6eacc17167fb6941017dc05ec7670b8fafa7b450dc4d24d；
- G-fifth-translation-original-expressions.json.gz：76352 B，
  SHA256 b266eebf27d001ef90fcc94f8b49b9f9984ed5d3f7a047d9b5cef5ddffd2423b；
- raw JSON：427950 B，
  SHA256 6e19e56d879eed7f7d741957526679521f65f06b92c42b4cb29f39fb2c2276e4。

原 50 列的 records 保完整两 mode。仅通过原 roots["-2"] 解码上列九个响应，逐 root 验证原 digest、label、参数与 third 权重和。绝不调用 mixed_response、原 producer 或任何旧 response NF。

## 5. 新观察本身

复用已经公开付清的 R406 入口 scripts/literature_weight_zero_natural_flux.py：

- blob 60ede13132d6eb38c8628eee9ccb0f0197c1bffe；
- SHA256 be12b9338cf5558eacb4d05b43f201871fae5d4262dd330304eaa56df3c2e12f；
- 所有 31 个原依赖 SHA 不变；新 request 另绑定该 mapper、只读旧 R210 源和本次新薄入口。

只调用一次 TotalFluxMapper.expression(corrected_mixed,true_weight=-4)：

1. 对已经 pure 零的完整 mixed 根取同一实 profile 对角；
2. 原 signed integral $I_{r_*}^x$ 中新增一个 $I(u'''M_{-2})$；
3. 使用原同锚、固定颜色、五次字语法；完整推出左 collar 后乘 $4$；
4. 所有外 $x$ 正幂、多字及原常数均保留；
5. 只有剩余全为 $x^0$ 乘单字时才取局部密度并算完整五次 Euler。

真原成本权 $-4$ 对应此自然泛函权 $-6$。这一权平衡在每个原左字中逐项核验，不能沿用旧 R406 weight0 的标签。

此入口不使用 profile 多项式见证，不把非零余字 NF 当非零泛函；若仍有非局部或左多项式词，结果准确标 unresolved 并输出全部词。局部五次密度 $L$ 满足 $5\int L=\int u\,\operatorname{Euler}(L)$，端项由真紧 jets 支付；因此此时 Euler 字面零或非零才是 universal 判据。

## 6. 预算、调用与输出

纯 Python 标准库，无 pip/sympy/numpy 新依赖。调用：

python topics/visible-flex-new-mechanism/scripts/literature_static_minus4_natural_flux.py --request PATH --out PATH

原资源界保持：
120 秒、512 MiB、8192 bits、100000 terms、300000 IBP calls、250000 cache entries、95000 B 完整报告、8 MiB 原 log。
只允许 GITHUB_ACTIONS=true 且本公开 repo。

入口绑定 source/request 后只执行一次。冻结 R406 mapper 的八项人工已付，不重跑；此次没有新代数实现，因此没有另设人工重算。新薄接口的所有输入状态、原字节/hash、原列 scale 和 index 都在科学前完整校验，错配失败且不消耗一个“替代目标”。

输出完整 correction roots/digests、一次原 primitive、全部左字/局部密度/Euler、unresolved 或 universal 结论、各阶段时间和原 mapper 统计。任何资源或输出上限都报告有限失败，不能截断后保留 nonzero 结论。

旧研究重算计数全部为零；一个静态 mixed 根与九个已存 mixed response 的必要输入解码另计。这个新观察不同时推进其它正常族或任意 coefficient。实际 public run 的 source、job、日志和读数仍由根代理记录；本设计不预授 $a_1=0$、剩余 PSD 或 whole joint 结论。原输出只在 runner 临时文件与完整 public log，不提交 Git/Release/artifact。

## 7. 文件交付

- 新源：scripts/literature_static_minus4_natural_flux.py；
- 固定请求模板：computations/request-static-minus4-natural-flux.json；
- 本设计：notes/static-minus4-natural-flux-design-20261116.md。

根代理可以把新 workflow/request 的自身 SHA 另加到 source_sha256，但不能更改上述冻结源或单目标/预算字段。所有修改先审代码后由根统一提交、actual pull、公开执行；本代理没有执行研究。

## 8. 新薄 workflow：规则读取和执行封口

.github/workflows/visible-static-minus4-natural-flux.yml 复用已付 R406 的 checkout、Python 3.12.14 和 read_original_actions_log.py 规则读取。新 request 已绑定原 reader SHA、workflow SHA、冻结代数闭包和本入口 SHA；workflow 在原 source commit 上读 request 并把它的原字节/hash写入 header，actual public/private pull 后重新 detach 原 source 并逐文件核 SHA。没有构造不可实现的自身 SHA 循环。

公开 pull 真正执行 git pull --rebase，输出 source/after blob、两 README diff 和起止时间；私有 pull 真正克隆稀疏规则目录、pull、核原 README blob 与唯一进行中 QUEUE，日志不公开私有内容。双规则任一变化即停止本次研究，由根处理真实差异。当前公开两个 README blob 仍分别为 21bd547f56590b7f2dd279d0297efb289a9b2783 和 d0432faff569c8e9af7ed4809847e12880976c11；原私有 README 预期为 5ba164843b1f5802184178a82d786264404873a3，课题 README 原不存在（null）。

规则完毕且来源一致后只启动本新 entry 一次，不调用旧八项人工，也无独立 py_compile 阶段。MR_TOKEN 在规则读取 finally 中移出环境；运行时只让原公开 log reader 使用 GITHUB_TOKEN，重定向不携带它。workflow 的权限只有 contents/read、actions/read，既不发布 payload 也不写仓库。新文件仍仅为未挂 blob，根代理独占正式挂树、提交和触发。
