# 请求105：从实际101的短参数recipe继续原搜索

**类别：计算接口；未预填新结果。** 实际101八次1/16接受仅因外预算结束，原unit/full112/native均未通过，见[正式结论](2026-11-15-actual101-same-eta-eight-acceptances-compact.md)。本轮从实际p=[0.5003346243435612,-0.2840549745844459,0.5965308971991595]重新求值。

新源 `computations/geometry_20261115_small_core_inexact_p3_eta_0p01_recipe.py` 为47106B，SHA256 `3169b2d3ea821a244d9f27611cd6c5cb3b239cf0e7f9bbbd7f49ac9d5f1dc9ee`。由真实source17a07c22的f43旧入口作15项明确文本替换得到；旧源完整保留。变更仅为文档、basename/schema、来源角色、recipe解析/CLI及初始参数读取。12个原helper/数学函数和class、整个search/final/except/finally正文保持，旧f43/ce93入口均不执行。当前闭包15源，请求74pins。

原三个unit方程和完整J、normal+Schur LM、真实d3、内层最后有限点及自身J、完整三方程merit/.2 Armijo、η=.01、外8×20/内12×20、1e-8原unit/full112阈值、FD、Arb160/depth14、原完整circle检查全部保留。设计参数搜索仍不是固定g的最终族。

`computations/actual101-explicit-parameter-recipe.json` 为1249B，SHA256 `98209dc9d214041865fea6cd2d5db34cfe7fdccc37ac3095e86e739cd2534091`。它记录真实101 run43679869518/source17a07c22ef60eb2f913703956c1284b8da533f32、status871932B/8044b98a981920f3b9d51a6d08533effdcd2965b4a46ddce4caafa3a0b66a017、log-summary53803B/d03b285893c2bd728532f44bb9a6438a5a789d91570e259b3364da5cbb1fbcbf和三个literal末参数。当前producer只读取这个短recipe和四原数学输入；来源status/log的SHA只是来源，不宣称这些payload被重新读取，不复用其J/merit/state/FD，更不伪造完整parent-status。输出明确使用新schema `R278-original-three-equation-inexact-p3-explicit-recipe-LM-eta0p01-v1` 和 `parameter_recipe`。

共享workflow SHA256 `3265acc514a21aea408ea508b2deae7798a92ef963db807c19bb152a44e54007`，request SHA256 `5941090a265a0d4be8e1d82e6e2afa3ae740f91d79acb7012feb2c5cbcf47d0f`。CLI改为 `--parameter-recipe` 与其SHA，其余科学参数不变。四输入若main清理后缺失，按原size/SHA从历史8bd267107cc8710d371f3b62c02986655ac965b0恢复。AST和科学在Actions执行；终端不可用，未宣称本地运行。只在日志复制原关键值、完整trial顺序、实际circle/scalar-domain元数据和hash；标记 `BEGIN_VISIBLE105_SCALAR_SUMMARY` / `END_VISIBLE105_SCALAR_SUMMARY`，无artifact、Release或Git原数据发布。

105实际正常运行后，106拟连续执行最多64个同源八步批次：每批只在真实stop为原预算结束且unit尚未达标时，由自身真实末p/statusSHA/已输出摘要SHA形成新recipe，fresh评价；异常、非预算停止、unit停止均原样处理，不新增接受门，不预设收敛。低三方程即使达标，完整非零BVP及本题闭面/全t/reach/同g加密目标仍须继续。
