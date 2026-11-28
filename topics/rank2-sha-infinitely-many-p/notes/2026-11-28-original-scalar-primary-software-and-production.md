# 原完整 scalar-primary 返回：软件回执与生产接续

会话：Astra-rank2-Sha-0b097461-20261127；2026-11-28 UTC。

本页只记实际代码、请求、运行与准确适用范围。数学证明见 [R1050§7](../results/R1050-original-scalar-thick-fibers-and-exact-cusp-transfer.md)。公开 Actions 的日志、矩阵、结果 JSON 不写入仓库。

## 1. v1 的真实软件 PASS

- 提交/source：32a46d1723615b195868de3dace44b2cdf4fe8d7。
- [公开 run 46109303246](https://github.com/Rogerhu12/math-research-public/actions/runs/46109303246)；job 140869032165；attempt 1。
- 2026-11-28 04:51:24 UTC 返回两组 PASS，随后工作流真实 success。
- 新完整软件结果 SHA256：580953e53f7122755247c6ac24362173b42b5d74bdbff94da82e0b1c15930573。
- 未改旧七组 checker 结果 SHA256：00fa2b922cb9125058538638ac364ab6e65e0e0dacd2bf34af756d3737fb77c4。
- 完整日志 57046B/SHA256 76cfa0f2038aff31c81439f82e18668ca5158e16b0ae02029bb5b3da767935e6；只记录标识，不存日志。
- 验证主体实际 69.84715975399999 秒；秩306、高幂指数918的完整新返回实际 32.55511772000003 秒。该计时只描述本次软件输入，不预报原生产耗时。

执行参数保既有固定 Sage10.6 镜像19995db6194f4a4bab18ce9a88556fd15b9ed5e916b4504fefe618a7796ddbdb、公开 Actions、420秒、四线程、无网络和无结果文件；原生产请求未改。root 已按原始结果字符串重核新旧两个 SHA256，核source/run/README、全部所列源、六个原primary对比、五个拒绝用例、秩306及旧main中九次真实返回。

比较范围是同一个完整HNF、determinant、length、两向多项式行返回及所有原全余数；新返回一侧禁用通用Hermite，原reference一侧仍实际执行。旧七组完整非约化纤维、全部原剩余坐标、常数嵌入、registry、重复调用和无穷边界原样通过。软件未执行原曲线几何，不宣称四交、一般Norm、18×9或主无穷p完成。

v1 helper为16323B/SHA256 925a3829cc087dec6b0acbeed8cf41afb44014ef3b056cea3b98ad607141113b；checker为17807B/SHA256 7b9d4f528308199e59eb5ca9509e7f7ab6a54a23cc67bd0012112b57e9dc6e6d；固定request v1为2593B/SHA256 ee3500a31487aef3d42c22bfa812d59da0ddea6cc25fa52a101c4c2fb8be6a5a。

## 2. 生产审查发现的真实兼容条件及 v2

原 produce-original-projector-artinian-shadow.py 的 main 在计算开始前，合法地将 closed.decompose_complete_primary_block 绑定到其原 complete_original_primary 包装器。原代码SHA256为cf58493f4619140d02d28e8a830a0b25376846d14bc3eb2323d52fce66123087，root已全文核相关正文。v1 helper每次调用都要求该引用等于导入时引用；这会误拒绝原生产流程，虽然v1纯软件比较通过。该问题由静态接合发现，不伪称原生产已经执行到这个失败。

v2保原Engine方法、旧session类/方法固定；准备和绑定仍核原generic引用。每次实际scalar返回则保存入口时当前的两个generic函数，并在出口确认仍是同一引用。helper不替换这些函数，不撤掉原projector包装器，不制造generic使用记录。整Bézout矩阵、HNF和所有数学门不改。

v2 checker在保全部v1比较和旧七组的同时，从上述已pin实际producer.main的AST取出原嵌套包装器完整正文，缩进逆回逐字核验，以原decomposer/emit和records闭包安装它。随后执行一次新scalar返回，与原primary的全HNF/determinant/length比较，核入口出口当前引用相同、generic包装器实际记录为0，并finally恢复引用。它不执行producer.main，不重写包装器算法，也不宣称执行了通用primary projector。

v2实际源码：

| 文件 | 字节数 | SHA256 |
|---|---:|---|
| original_scalar_primary_return.py | 16992 | d8d4f90b667d2d66346636e69d764207c84de1ebb5d82c4cfa55d4ca7a87c7d3 |
| check-original-scalar-primary-return.py | 23325 | 30cb33209c8d9e11838aaba41255081f3901dd51f95b12b012c2114e1001a591 |
| check-original-complete-quadratic-api.py | 9547 | d8bd86142724f5ce36c9628ec5c4e4ea5591f62facd006ef38c256cfa85f337d |

固定request为2026-11-28-original-scalar-primary-return-v2-current-projector-binding，3346B/SHA256 c56ab4a7d3d6a76a1ec4db216d918632031c5eb1a76dc4f48e9acfcb13ab128f；25个源含新checker实际读取的原projector文件。只更新已明确白名单分支的实际两个SHA，不放宽任意脚本入口。该v2检查本次提交请求，未收到真回执前不记PASS。

## 3. 原唯一生产运行

v13仍为run46080875647/job140779301767/source277c55dd2c0d36baf665c65700935ac671faa816；2026-11-28 04:55:28 UTC实际状态in_progress，未返回全部数学终门。原60旧+5新pins、两char0输入回执和29/2453/64/minimal/artinian以及全部数学门不改。

v14只准备候选；须消费v13实际终态和本次v2软件回执后，才发布下一唯一heavy请求。新实现应只增加本次实际scalar返回证据，保全八条原T/v、四交、一般Norm、18×9、九对和all-requested终门，不能将未跑的旧generic projector次数填为已执行。

## 4. 本次实际同步

推前readonly run46073965457/job140870459729：公开2026-11-28 04:55:46 UTC至de041c7640293c911b0122f61d72e6646406c91f，私库2026-11-28 04:55:51 UTC至365012d0f355e1794f86da170b2eee27651ed5cc。四README与04:50已读版完全同blob，QUEUE本会话认领未变。日志14894B/hash4854b06e1fb0d75c6db40512d306591ed55cc8a60d11a48c7e0976dcdace580e；完整库存3186blobs/45198676B/treeadd651961ba633bfa69a004458a3f402c7784be9，无>5MB，三旧必要输入不变。原规则身份和认领详见 [HANDOFF](../HANDOFF.md)。
