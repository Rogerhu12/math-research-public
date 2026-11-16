# R150：十行、十二参数、50 原列的有限域来源正门

作者：Astra-ISP-789f / normal_annihilator，与 /root 协作。AI-assisted：GPT-6 Astra Pro。日期：2026-11-16。

## 1. 入口与本次权限范围

读取已经完整验证的十行 116 原种子模型及其 50 原选列压缩。基环固定为

$$
B=\mathbf F_{127}[y_0,\ldots,y_5,w_0,\ldots,w_5],
$$

只把原固定三次数域的常数按已合法核验的 $d\mapsto100$ 约化；不专化任何 $y,w$，也不专化五个原 $u$。十个生成元依次为

$$
m=(1,u_0,u_1,u_2,u_3,u_4,u_1u_4,u_2u_3,u_2u_4,u_3u_4).
$$

50 条柱 $g_i\in B^{10}$ 均为 116 条中的字面原列，各自保存完整的原 18 来源 $\sigma_i$，满足

$$
m g_i=A\sigma_i,\qquad
A=(F_0,\ldots,F_4,\partial_{w_0}R',\ldots,\partial_{w_5}R',
\partial_{y_0}R',\ldots,\partial_{y_5}R',y\cdot w-1).
$$

50 与 116 生成同一个初始 $B$ 子模。此事实不意味着该子模对五个 $N_i$ 稳定。程序仅搜索一个充分的正证：$e_0$ 是否能由这 50 条原列组合得到。非零候选余式只记录为诊断，既不排原理想成员，也不排更大的稳定闭包。

## 2. 冻结来源与输入

| 项目 | 路径或身份 | bytes / SHA256 |
|---|---|---|
| 主源 | notes/2026-11-16-r150-original-compressed-parameter-module-positive127-789f.py；blob f9ccc9952b718265aeec08780ad7ca22661dcb1a | 31539 / 4741ca5f21a087f7c8a5248f1a8fb2559b60635ff60552643061c407dfcb3626 |
| inputs | notes/2026-11-16-r150-original-compressed-parameter-module-positive127-inputs-789f.json；blob fbc5361a4ccf535abf7ddf959d5aad80fec08f09 | 3005 / cc39334ae9301040971e1ec104fdc4b9787d452ed638ae832c2d52073b65e4ba |
| 原十行模型 | notes/2026-11-16-r150-original-ten-generator-parameter-module-field127-v2-789f.py | 23879 / 4a7c1d93e65079912c66ad3370ba7cf59c3c5ef7d385c7cf69ba3cde76dac8e4 |
| 原压缩 | notes/2026-11-16-r150-original-parameter-seed-compression127-789f.py | 20434 / b1d3dbedd597a8019bab2dca6ff59bfa915aaa457a8ac0c14833266f449a1ee9 |
| 独立 session | notes/2026-11-16-r150-original-parameter-module-session-789f.py；blob bbaa0dd4adfc4ee1899c82290417c97f24288d3e | 19630 / fe16ae37f209982ec4cfcf38b60763081cf159408d441bff3440bdf7002424c7 |
| workflow | .github/workflows/invariant-subspace-r150-original-parameter-module-session.yml；blob dd446d336480992e72175b3b9c98aa1b7b32ab7d | 2121 / a3687ae72beacad25fb40588d4b7b9608775607deebbc3d0c0d138c643d39aee |
| request | notes/2026-11-16-r150-original-parameter-module-session-789f-request.json；blob 6d3936606fb84477b487a3dcb23d54b97f81b748 | 8159 / d1e45f2c73314b5b3d6ce2475a772caccb9028dcfb28950dc1be893db1c0f1bf |

原模型 binding 为 7c59f3f6e05c836aa97eef0ad358eaae8f8174c8225b1842ed5c4f313000f3d4；其 30466-byte 数学 manifest SHA 为 9120695ac2e42f8300fdea4aa814183bc033d83062810a8854998a25199795e2。原压缩 binding 为 baaa8ec3f9459c0d2f88ebb452c941ce241f2727d5becab1ca78511a55a589ca。

压缩阶段的计时及 native 回执 SHA 在诚实重算后可以不同。因此本入口不伪造旧计时或强配旧压缩 manifest 字节；它实际读取完整新回执、核其 source/binding/完成标志及完整文件 SHA，并另外钉住下列纯数学 JSON：

~~~text
{parentBinding, prime, coefficientRoot,
 allOriginal116SeedExpansionColumns, retainedOriginalSeedIndices}
~~~

该 canonical JSON 为 620742 bytes，SHA 为 a1d73ea1ce5809c87bdc34724c1eb4407d6a5c0ae78fbf16aa3650563aa089dd。一个已开始的候选续算则还要求其实际输入描述符逐项不变。

## 3. 原来源正门

先逐列独立重乘全部 50 个 $m g_i=A\sigma_i$，并核原 17 梯度的完整 Jacobian 运输。随后在全局次序

~~~text
(wp(1,1,1,1,1,1,2,2,2,2,2,2),C)
~~~

及 degBound=0 下构造完整十行 50 列 module；不把方程 $y\cdot w-1$ 当齐次式截断。

程序先调用 slimgb(module) 寻找候选，完整 SSI 保存并逐柱核读回相等。该候选中即便 $e_0$ 余式为零，也还没有来源正证。之后只对这一列调用

~~~text
lift(Original, Target, Units, "slimgb")
~~~

并要求返回 50×1 的完整来源、Units 恰为 1×1 单位矩阵。来源先以 SSI 整体保存、逐项读回；然后核原十行乘积，导出全部 50 个来源多项式。

Python 解析器只接受 short=0 展开的有限域单项式，不执行文本。FLINT 独立验证

$$
\sum_{i=1}^{50}c_i g_i=e_0
$$

的全部十个坐标。再构造全部 18 条

$$
S_\nu=\sum_{i=1}^{50}c_i\sigma_{\nu i}
$$

并实际核验完整多项式恒等式

$$
\sum_{\nu=1}^{18}A_\nu S_\nu=1.
$$

最后使用已付全局多项式坐标逆的 Jacobian，把前 17 条来源运回原物理梯度，再独立核验原物理 17 梯度与原 Bell−1 的完整乘积为 1。证书保存该真实来源和全局多项式逆；原坐标来源可以作为精确替换 SLP 读取，不需要把巨大替换多项式另行全部展开。

因此任何完成的正证不依赖对候选 G 的所有 S-pairs 做独立闭合认证，也不依赖先证 50 条对 $N_i$ 稳定。其逻辑只用字面原列及逐方程恒等式。程序仍不从模 127 的单位恒等推出特征零单位；后续 E 来源必须另行实际求取和完整乘回。

## 4. 必须先实际通过的 module 自测

此次对象是 module，不能沿用旧 ideal 自测冒充。因此新 job 先在两个参数上构造

$$
\operatorname{Original}=
\begin{pmatrix}
x&1-xy\\1&-y
\end{pmatrix}.
$$

$e_0=y( x,1)^T+(1-xy,-y)^T$。程序实际运行 module slimgb、原 G 的 SSI 逐柱往返、target-only lift、Units=I 和全部原两行乘回。另以单列 $(x,1)^T$ 作不含 $e_0$ 的独立负控制，防止 module/rank 转换错误。最后由 FLINT 独立解析并核这两行来源，以及带负系数和混合幂的输出解析小例。

此处 degBound=0，不使用有界次数续接语义；旧 2→3 ideal 测试不充当本程序的完成门。实际 Singular 二进制、版本全文 SHA 和 SSI 必须属于同一 session。尚未执行的自测不会在回执中预填完成。

## 5. 阶段、断点与失败范围

阶段依次为：原输入全源核验；module 自测；50 原列 SSI；完整 slimgb 候选 SSI；字面 $e_0$ 余式；单目标来源 SSI；全部十行与 50 个多项式文本；独立十行乘回；18 原来源累积；原梯度运输及最终完整证书。

只认已注册的完整文件和实际 SHA。每个阶段均保存实际源版本及绑定。来源文本按连续前缀登记，独立十行产品与每条原来源按完整坐标/方程登记；不把进程中未返回的 G 或 lift 当作已存前缀。每次续算重新校验实际输入和必要源文件。内存、语法、原来源或乘回错误记 failed，具体 type/message 置于 parameters.error；时间预算只记 budget-checkpoint，不解释为代数障碍。

Actions wrapper 相对已审 Bell4 版本仅改独立身份，并增加真实进展门。600 秒后只有 exit75、同一 binding 且完整 candidate 已存在，且 candidate/source/文本/已验证 phase 描述符出现新进展，才允许 1200、1800 秒的下一次执行。只有输入 SSI 或未返回的 slimgb 不足以启动续算。后一次仍无新完整进展则停止，不机械重复相同失败区段。

## 6. 三步独立 job 与 CLI

无需历史大数组；在一个临时 job 内按已锁小源码重新生成：

1. 十行模型 180 秒、2 GiB，全部 116 种子完成。
2. 完整压缩 180 秒、768 MiB，全部来源校验完成。
3. 此正门首 600 秒、4 GiB，后续只按上一节的真实进展门续算。

整个 workflow 90 分钟，内部算术会话上限 80 分钟，并在 workflow 起始后 88 分钟前留出收尾余量。只有完整下一预算加 120 秒仍适配时才启动。运行及发布前真实 pull、核两份 README，长任务每 28 分钟重核。仅源、参数、执行身份和输出 SHA 进仓库；所有数学数组、SSI、二进制、原回执及多项式文本留临时目录/完成 job 日志，不建 Release 或计算工件。

~~~text
python 2026-11-16-r150-original-compressed-parameter-module-positive127-789f.py
 --model-source {scripts}/2026-11-16-r150-original-ten-generator-parameter-module-field127-v2-789f.py
 --model-out {work}/original-ten-parameter-module127-v2
 --compression-source {scripts}/2026-11-16-r150-original-parameter-seed-compression127-789f.py
 --compression-out {work}/original-parameter-seed-compression127
 --out {work}/original-compressed-parameter-positive127
 --singular Singular --seconds 600 --memory-mib 4096 --through final
~~~

同源码允许 --through prepare 或 --through selftest；这两种前缀完成均不声称原理想单位。

## 7. 已实际完成的本地准备

本地同一冻结主源已执行 --through prepare，预算 180 秒/1024 MiB。实际 11.621044523 秒、exit0，峰 129308 KiB；全部 50 原 18 来源和 17 梯度运输真乘回。315888 个参数向量单项式、65853 个来源单项式全部保留。

完整 ASCII module 为 5080340 bytes，SHA 54fe7a3d100b2f28bca8cb5d2effd8fd170eac1f9ddb55afe5c05cf728e9a801。实际 binding 为 bda795b66027438ccde3690039afdad45fa2b80ecf952ef2f12e88ce2e605d35；原准备回执 31018 bytes，SHA a58bf7957a14e7c83889d4f930bce5a50215600224dc27898f1aa590cdc68113。

此实际前缀没有调用 Singular，不包含自测通过、候选、lift 或任何新单位结论。

## 8. 官方接口依据

已实际读取 Singular 官方仓库 doc/reference.doc 的 slimgb 和 lift 节；其 blob 为 67a64ee0438e7349d9fe2a1d53bcc1ddc98ca7dd。slimgb 明确接受 module，并要求全局单项式次序。lift 对 module 返回矩阵来源，规范身份是 matrix(Target)·Units=matrix(Original)·Sources；多项式环下 Units 为单位矩阵。本消费者仍将这一点作为实际硬门，并独立核原乘积，不以文档承诺替代算术。

[官方原文](https://github.com/Singular/Singular/blob/spielwiese/doc/reference.doc)

## 9. 根审计与实际派发门

/root 已全文读冻结31539-byte主源、19630-byte session、workflow/request及本接口；另以标准库核本地源码AST、prepare原回执31018 bytes、manifest15772 bytes及5080340-byte全原ASCII模块的完整SHA和实际binding。全部50原18乘回、17梯度运输与参数/源单项式数均与原回执相符。三步job只在本发布实际pull、规则核验和push成功后派发；运行号和结果以后续实际身份记录为准。此审计未提前运行或声称Singular自测/候选/来源正证。

## 10. 首次真实作业与固定运行时重建

实际 run43876083196 的完整模型成功，但压缩入口在父manifest物理SHA门停止；尚未执行Singular自测或候选。[完整失败记录与118文件核验](2026-11-16-r150-original-parameter-module-python-runtime-failure-789f.md)精确定位Python3.14的gzip OS头差。当前workflow仅增加setup-python@v5并固定Python3.12.14；原所有数学源码、request、输入字节pin和binding均保留。新版仍从完整父模型重新运行全部三步，只有实际命中旧manifest物理SHA并完成原门才推进。/root另直接对完成日志的全部118实际描述符逐一核对，只改内存OS头后所有stored/logical SHA均相同，实际0.65624055秒/exit0，原文件未改。
