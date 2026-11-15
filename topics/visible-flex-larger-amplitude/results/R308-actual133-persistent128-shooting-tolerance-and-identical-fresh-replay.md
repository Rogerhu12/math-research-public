# R308：actual133 持久 binary128 shooting 一步达到原容差，独立重放逐字一致

作者：GPT-6 Astra Pro（exact_refinement）  
日期：2026-11-15  
类型：启发式/数值证据；完整实际日志读回，不是精确解或最终 native 证书

## 308.1 实际结论

actual133 从明确绑定的原失败状态作为初猜，重新形成完整 fresh64 $J$，并在独立进程中持有完整 binary128 状态。它用**当前 binary128 原 residual**形成近似 R273 的 RHS，得到一个完整方向后，第一次真实试探 $\alpha=1$ 即被原严格范数下降规则接受：

$$
0.000122096054597410989492629881621789239
\longrightarrow
9.68582474751023176032080482454992093\times10^{-11}.
$$

两次值都来自完整 576 段、129248 个原 cut/stage/far 行。原报告的 `below_original_tolerance` 从 `false` 变为 `true`；停止原因是 `shooting-tolerance-reached`，不是墙钟部分结果，也不是十档全拒。

随后另起进程，从真实末 binary128 状态进行独立完整重放。全部 129248 residual 字及全部 576×226 stage 输出字，与 owner 的末态读值逐字一致。

**尚未完成原 native/fullDN。** 本次没有请求匹配 trace JVP，也没有请求完整 stage 列；完整 338×112 endpoint 响应、原几何 final audit 均未执行。所有相关原 flags 保持 `false`。这项结果支付的是原停止准则的完整高精度 shooting 部分及独立重放，不能冒作完整原 worker 成功锚或最终物理验收。

## 308.2 真实 run、日志与短报告身份

| 项目 | 原身份 |
|---|---|
| run / attempt | `43704718358 / 1` |
| source commit | `4f0ea9a175e3b3bd9f38515bd61833a392e8dbd6` |
| compute job | `132783217957`，所有执行及清理步骤成功 |
| report job | `132797117252`，成功 |
| 请求 SHA-256 | `fff427808de30da8054ba19f3edd6123f7cac7e0a999c2eb5ff1b5730260cc50` |
| compute 原日志 | 183248 bytes；`8e168747b6d4a22812bf506f2d75c6b9d68c90440a8af52860188e38c5d1de5b` |
| report 原日志 | 61492 bytes；`a705241806f51d23733e92ffdc142c9ebfaeb7141ccd7b8f6f70c2de8fae6434` |
| `BEGIN_VISIBLE133_SCALAR_SUMMARY` 内原 JSON | 28389 bytes；`8f88fa6a4010099bbf104b39270ef611478e16d6cb19faa01e4d4d409c953d5b`，不含分隔 LF |
| owner compact summary | 14677 bytes；`0147f874560950905dd2dc5ff69b6ead949cddf135fb0a0570e0dc5b3fd800b9` |
| 完整 owner summary | 110035 bytes；`d9f8fc5a887a4ffbe7dc4e7628cd5ac5a749f9f8a6817741b54cb7782986f25f`，runner 临时文件，已清理 |

原 compute 日志按事件读取，未把超过 100 KB 的文件整篇展开。它含 21 个 `native_persistent128_worker_record`，其中 7 个是消费前即打印的原 owner 记录：initial、need_direction、direction_lifted、trial、iteration_closed、owner_final、independent_fresh_replay，各一个。

原 compute 的最终短 JSON 与 report 中原 JSON 逐字段相同，其 bytes/SHA 也与 compute 事件宣告相同。initial 与 direction 请求的 current 相同；trial、iteration-closed、owner-final 及独立 replay 的完整 evaluation 对象相同。这些是 JSON/字节/事件一致性读取，没有本地重算范数、矩阵、RHS、QR 或 Fraction。

## 308.3 真正使用的状态、模型和方向

### 初猜及 fresh64 来源

原失败73状态只作 literal 初猜，原 binary64 raw SHA 为
`f6abeb044a692342f2e3184776bacb34ddb2cf499517fecbc41fb36e7e279ad6`。
不把失败状态、旧113 packet 或已删数据的 hash 伪造成成功缓存。

本 run 的完整 fresh snapshot result 为 1316 bytes，SHA
`0c86c1ce79b99deb01d4119445ad7fb7d462e20c37081a2e95c175b18ada92e3`。
实际记录的全部 stage-J raw SHA 为
`1f5e3cfd7d7fec8c127841c3c859b43ed4264e55c7bf7805e84f4dae73b453d4`。
同一来源完整保留 H、target、原 $\sigma$、far graph 和原几何；H SHA 为
`c35972d038321acf6db273248189b1e1d2527aa6eb2b323d37fcde4da448682f`，
原 $\sigma$ SHA 为
`ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc`。

fresh64 基态原 norm 为 `6.0618737006888706e-05`，它与独立128评价的 norm 是两个不同有限算术对象；本结果没有把前者改标签成后者。

fresh64 还形成一次原 R273 方向，其 raw SHA 为
`4bb396b069f5c32a3d77a08531ad2cdefbd3ece7fd8f63c56baed84f13976ce6`。
这份方向进入 packet 的 provenance，**不是持久128迭代直接接受的旧 RHS 方向**。

### 当前128 residual 的新 R273 RHS

owner 初始完整状态为 2067968 bytes，SHA
`35a1f91163fd0dfc28ca911ddfd1d29f43e02e0cc0974d5db4e1145b9471f5a6`；
其完整原 residual 为同样 bytes，SHA
`7a2f785786ee1e60b63270925c9b1f6a9425ca5755cf50c64732f8aded520cf1`。

近似模型明确是固定 fresh64 $J$ 与 current128 RHS 的 chord 模型：129248×129248，行顺序 `cut112; stage576×224; far112`，列为 577 nodes×224。新矩阵身份为
`fd50a33ab001b3a0f278785eebe2b82d46430359e86913e4d2f1f009ac0d02ba`。
`fixed64_J_is_current128_derivative=false`；没有付匹配 current128 DF 的结论。

只为近似 QR，将完整 current128 residual 每项一次 RN 转为 binary64。原报告记录：

| RHS 转换项 | 原值 |
|---|---|
| 转换后不同的条目 | 128969 |
| 非零变零 | 0 |
| 最大原 $\sigma$ 缩放转换误差 | `4.10665514535721833358792197700840237e-21` |
| 最坏转换行 | 2568 |
| `rhs-for-R273.f64` | 1033984 bytes；`d52e97215a5b0527a0e758fcd9e4713b648391cab796d6c404ad0a43d901ca90` |

原128 residual 与状态从未被这个64位副本替换。

### 完整近似 QR 与128恢复

该 current-RHS R273 的实际计数为：576 stages、577 nodes、577 个 node penalty blocks、1153 次 QR、129248 原行、129248 列、258496 增广行、129248 pure constant rows；全部因子和纯常数 464891392 bytes，`complete=true`，$\eta=1$。实际 QR elapsed 为 `6.404514242999994` 秒。

完整 current QR 报告为 465278 bytes，SHA
`87d114147e47735e6e71d5fe9267f444fc59a9eed905752ead9401aefb6003ba`；
1159 个临时文件的 manifest 为 164050 bytes，SHA
`277a9472a73799e9e6fefff2ddae8d3c8264c334a7d8257a19a53d19cd0e6b70`。
这些是 run 内实际报告的完整临时范围，并非在本地重新读了已删除因子。

R273 摘要中的 NumPy `dtype=float128,itemsize=16` 同时明确 `significand_bits=64`，即该 runner 的 longdouble；不能把它称为 owner 的 IEEE binary128 算术。

实际新缩放变量 `scaled-z.f64` SHA 为
`a55d9fc6d3519989d41881b0418bd9d33916d51ee8d5b92cde4d674750450d2a`。
owner 用完整恢复

$$
\delta_{128}[n,j]=\operatorname{lift}_{128}(\sigma_{64}[n])\,
\operatorname{lift}_{128}(z_{64}[n,j]).
$$

原 cut/far 分量不投影或清零。报告显示该恢复与先在64位形成的 R273 delta 有 129182 项不同，最大缩放恢复差为
`6.21420740974797949698112574685574514e-28`，没有从64零恢复出128非零的条目。缩放 $z$ 的原记录 $\infty$ 范数是
`1.1744305406651254531844570279775999e-11`。这些原 scalar 不被用作新的接受门。

## 308.4 全部实际128试探：只有一档，已接受

| 原字段 | initial | 唯一 trial `(iteration=0,trial=0)` |
|---|---|---|
| 完整段/行 | 576 / 129248 | 576 / 129248 |
| norm | `0.000122096054597410989492629881621789239` | `9.68582474751023176032080482454992093e-11` |
| norm binary128 hex | `0x1.000dd1f7889da0c80213a1f62c65p-13` | `0x1.a9fcb11a67aa9fdf970095730bcp-34` |
| below original tolerance | false | true |
| 最坏行 | stage11 / Pi104 / global2791 | stage9 / Q1 / global2128 |
| failed stages | 空 | 空 |
| evaluation error / budget exhausted | null / false | null / false |

唯一 $\alpha$ 原 hex 是 `0x1p+0`，decimal 是 `1`；`accepted=true`，原因 `strict-original-norm-decrease`。完整 trial elapsed 为 `804.281616974` 秒。

真实形成 trial 状态时，126690 个128字改变；其中11183个改变后的128值与基态转成64后的值仍相同。这个事实证明本次状态更新确实保留了一批64转换不可区分的低位；它不单独证明改进的唯一原因，也不构成普遍浮点误差下界。

初末两次完整评价各自都记录 27772 root calls、904 Newton steps、904 root line-search trials、29580 angular evaluations、最大迭代指标1、fallback0。末态返回原root的最大相对误差为
`7.97942273584970897156361583077509912e-14`；末态 min A/D/S 分别为
`0.999999999975949816097646428367803865`、
`0.999999999999985782663062751174097867`、
`0.999999999999999999999999999688946329`。

原 outer tolerance 的实际提升字是
`2.00000000000000012456318291555971284e-09`；root stop 是
`7.99999999999999999055447483647918958e-14`，fallback 是
`4.99999999999999969748484640969905465e-12`。没有改成 refined root policy，也没有放宽原阈值。

末态控制行原读值完整为

$$
r=4.99890220172700756918252291853272271\times10^{-25},\qquad
\sigma=5.16104960810073433235339041548094359\times10^{-15}.
$$

输入 node10、输出 node9、mode1，原 signed normalized 值与末 norm 相同。原 mean-height sum 初末均记录
`0.0226842463487103007695708959242220956`，hex
`0x1.73a8a00cef80fae4744e57d3f5bp-6`；这是两个原读值相同，不是本地重算均值。

## 308.5 精确保存范围与独立fresh重放

owner 原终态：`directions_computed=1`、`trial_evaluations=1`、`accepted_steps=1`。
请求方向仅 `[0]`，试探地址仅 `[[0,0]]`；方向1–31、最后方向的 trial1–9 未访问，原因是已有一次接受并达到 shooting tolerance。不能把这些后缀写成拒绝、接受或墙钟未完成。

| 末临时对象 | bytes | 原 SHA-256 |
|---|---:|---|
| 全部577×224状态 `final-state.f128` | 2067968 | `e0f20c36d59ac200796a03441e7b5604224e3add414361a11cc6ff3586dffba2` |
| 全部129248 residual | 2067968 | `18cfb3face9b286513f624003984d318bc6b6c735ed803a3cbffde15dc6be39b` |
| 全部576×226 stage输出 | 2082816 | `13195bbb4249c47b158399c36d173de0fc8bfc80e3b9f5ad98ed1411ff715f9e` |

独立 replay 直接读上述真正末 binary128 状态，未先转64；原 source 另起进程重新走全部原 cut/stage/far、两均值及同一原root policy。它返回完整576段/129248行、同一个末 norm 和控制行；原完整 evaluation JSON 与 owner-final 对象相同。

replay 的 residual SHA 和全226输出 SHA 分别与表中相同；原 run 的 `fresh_replay_full_residual_words_equal_owner`、`fresh_replay_all226_output_words_equal_owner` 都是 `true`。replay 临时4文件的 manifest SHA 为
`61aa5faf7325968543a839636a770a755298ba0db12c4c0756d9edd64ca5f481`。

这里只独立核对了原日志报告的字节身份及原比较结果，不冒作已在本地重取全部 raw payload 的审计。依根规则15，这些 runner 临时对象已清理，没有 artifact/Release/Git 数值包；其 SHA 不能恢复当前状态。后继必须在同 job 清理前接入，或重新按同一实际来源与步骤求得状态。

## 308.6 模型读数不等于真实接受或精确证书

current-RHS QR 的原 longdouble 读回包括：

| 量 | 原 `decimal_display` |
|---|---|
| formed residual infinity | `9.685824747510231713e-11` |
| formed residual two norm | `1.130568575521336125e-10` |
| objective | `6.461955386998909204e-21` |
| pure constant square | `1.2923910773994321724e-20` |
| factor triangular residual infinity | `1.0667321179483844895e-20` |
| formed energy − factor energy | `3.4966828013055790077e-33` |
| full unpreconditioned model gradient two norm | `1261309.1059448874298` |

这些是同一 formed f64 系数的普通 longdouble 数值作用。它们不构成 exact rational 上界或最优性证明，尤其完整 gradient 原大值必须保留。本次真实接受由另外的完整128原非线性评价裁定，而不是模型残差或梯度门。

fresh64 原 R273 的 exact affine 最坏值
`9.685623139820915231844260456306540893890861679791289092058094119E-11`
属于 fresh64 保存模型；不能换标签为本节 current128 模型或完整128 nonlinear 误差证明。

## 308.7 程序成功、规则同步和未付责任

原记录为 `procedure_complete=true`、`summary_complete=true`、`transport_complete=true`，无 launcher error、无日志转发错误、无任何 owner/replay/guard 墙钟截断。owner elapsed `2432.320432099` 秒，bridge guard elapsed `2432.56398849` 秒，完整 fresh入口 elapsed `3342.529520208` 秒；guard return0、child return0。

外层原64 driver exit2、response.failed 为
`PERSISTENT128_CONTROLLED_ORIGINAL64_STOP_AFTER_INDEPENDENT_OWNER`。
这是显式受控终止，原64非线性trial调用数为0；不是新的原64 line-search 数学拒绝，也不是原64 worker 接受。不得因 compute/report 两 job 绿色就覆盖这一层语义。

原规则监控实际完成两次真实同步，UTC `10:35:05` 和 `11:20:09`；原 source checkout 始终是本 run 的固定 commit，没有把规则同步后的 main 当科学源码。

| 责任 | 本次原 flag |
|---|---|
| 完整128原 shooting norm 在原阈值下 | true |
| 独立fresh128完整重放及word相同 | true |
| matched finite-trace JVP | 未请求：`matched_trace=none` |
| 全224 stage列 | false；请求0列，完成0列 |
| endpoint338×112 sensitivity | false |
| original geometric final audit | false |
| native accepted | false |
| fullDN completed | false |

包含两均值的全226 replay 是原 shooting 程序的完整重放，不能代替全112边界响应或原物理审计。原 C-based radial jet、有限 root trace 导数及真实几何审计仍按 R283/R302 的对象区分，不能挪用旧64结果补齐。

## 308.8 可复现来源与后继选择

原 workflow：`.github/workflows/visible-larger-public-native-persistent128.yml`；原请求：`computations/public-native-persistent128-request.json`，均以本 run source commit 为准。37个 source pin 在原启动记录逐项列明，78份原数值源按公开历史清单恢复。四个直接运行源为：

| 源 | SHA-256 |
|---|---|
| `geometry_20261115_native_persistent128_probe.py` | `2683e8e13a8d73d6c08500e9d3716d5bac5dc2e66648a17c8e1d75d246c62107` |
| `geometry_20261115_native_persistent128_bridge.mjs` | `2657ddeece61edcf608d8ff3a14e941acabd7eead86b17d2fdb666d6c4c76111` |
| `geometry_20261115_native_persistent128.py` | `767a4c4b329779fd200e6ec6f674ab62db9f6a65984628299d1f2241f83dd322` |
| `geometry_20261115_native_persistent128.cpp` | `7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd` |

原113 primal CPP 仍为 `1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d`，R273 factor 源仍为 `9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33`。本次编译确为 `-O3 -fopenmp -frounding-math -ffp-contract=off -fno-fast-math`，并链接 `quadmath`。

真实91输入 tuple、两历史 ready 的完整路径/SHA均保在原请求。两 ready 从历史 commit `8bd267107cc8710d371f3b62c02986655ac965b0` 读取，SHA 分别为 `563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6` 与 `c1c44f2384845c25d2dcb0ec7127934fa46b54aa74613efcd6f9f6bcf0eb541d`；未偷换原校准或几何。

在公开 Actions 里按原请求付清来源后，科学入口参数是：

```bash
python -u geometry_20261115_native_persistent128_probe.py \
  --original91-directory "$ACTUAL91_TEMP" \
  --source-topic "$RESTORED78_SOURCE_TOPIC" \
  --seconds 18000 --threads 4 --fresh-replay-reserve-seconds 1200 \
  --matched-trace none --final-stage-columns 0 \
  --out "$FRESH_RUNNER_TEMP_OUTPUT"
```

原 $\eta=1$、最多32方向、每方向原十档及 $2\times10^{-9}$ 原容差不变。重新执行时必须读当前规则并更新规则监控的明确已读身份，不能盲用已过时根README pin。

与 [R288](R288-actual113-complete128-policy-dependent-descent-and-original64-rejection.md) 相比，本次实际方向使用 current128 RHS，状态及恢复也持久保128；结果不再只是把旧64方向放进128 primal试一次。原数据支持继续完成真正当前128 final责任，不支持再以这一个点为由盲调 $\eta$、猜相邻word或宣称全局浮点极限。

已发布并独立运行的 request137 负责同job清理前的完整 stage/112边界/endpoint/物理审计接线；其未来实际结果仍须分别读取。[R303](R303-actual122-partial-finite-root-directions-and-controlled-stop.md) 显示匹配trace方向代价很大，故 R305 的新共享算子是独立性能实现路线，不能提前充当已完成的 Jacobian 或误差证书。课题整体完成标准仍未达到。
