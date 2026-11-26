# 03b 宽支撑端点初根实际失败与独立半径输入

日期：2026-11-26。范围：记录公开实际返回，并给相同完整科学源码的一个新数值输入。这里没有已接受的零闭合场，也不把求根残差当作题目所需的连续等距或几何证书。

## 1. 已返回事实

完整实际来源是 [公开 Actions 45820592817/1 的 part002](2026-11-26-public-actions-45820592817-1-part-002.md) 的阶段 8、9。阶段 8 的步骤标识为 `complete-independent-zero-closure-SO3-wide-support-first-20261126-recover03b`。

| 项目 | 实际返回 |
|---|---|
| 状态、退出码 | `failed`、`1` |
| 阶段实际秒数 | `11.012000173999922` |
| 完整失败报告 SHA256 | `e21cc593c2a71f0922920f8f4782ba03d3f731b7b5e932ee7bc45e653864ab60` |
| 报告字节数 | `81691` |
| 实际源码提交 | `eb2ab98a943667c0d4a7097c8e8ade371a9b0c2a` |
| 宽支撑表示身份 | `0595aab48af53b68cf5be53e2663580d7c14258169a613ea3884424f9d005717` |
| 固定参考 bundle | `0f0424cc7403d0ffbca22490fc9d0bc154c52c356278a800553528e77fc386c1` |
| 固定准确 scalar 目标 | `6ffc1f7fc1e6196318dc27da22b6c9ffda3ee64e81223a4c815f6348cf5baebb` |
| 原自由坐标点身份 | `cd530c070cfa54f122f19fe16e9b312e360f93e072496e445d1cc6c36973c0b3` |
| 首批实际逆图角数 | `8` |
| 未通过本轮求根的角索引 | `[6]` |
| 失败时批内最大实际端点残差 | `0.03491092443943436` |
| 失败时批内最大实际修正范数 | `0.49996846575301557` |
| 实际异常 | `No actual endpoint-root backtrack decreased the same complete equation` |

阶段 9 的相同 `b25e5a5f…` 纯 reader 于 `6.006831188999968` 秒正常返回。其紧凑 readout SHA256 为 `c612ec9e4f31d683f983296d41b5db1c6106ad9166defa6580529ba06969975d`、`20830` 字节；它再次确认 `complete=false`、初场与末场均为 `null`、真实 `J/Jtranspose` 调用均为 `0`。这些返回不含一个可接受零闭合场，不存在从这次失败场继承几何或度量结果的步骤。

两个最大值是失败批的全批读数；现有标量返回未逐角给出它们，不能断言最大修正必定属于索引 6。该残差也是最后失败迭代处完整方程的数值残差，既不是准确的初始闭合缺陷盒，也不是严格不存在结论。

## 2. 半径在已刊源码中的职责

本次实际使用的端点核为 `so3_zero_closure_endpoint_operator.py`，SHA256：

`5b4c3921a0f56a9ac3acc12c03e788b3b648b15817b2e89e155a18feb2b24c46`。

它的 `EndpointPolicy.__post_init__` 对 `branch_radius` 检查正数和有限性，没有把 $1/2$ 规定为固定准确目标或物理约束。`_solve_roots` 从每个角的字面零初值出发。每个 Newton 回溯候选须满足

$$
\lVert z_{\rm candidate}\rVert_2 < r_{\rm search}.
$$

这是候选搜索域的数值输入。无论半径是多少，实际接受的根仍独立要求同一完整端点方程的数值欧氏残差不大于 `2e-12`；回溯仍要求原 Armijo 下降或已经达到这个残差验收。数值 Newton 迭代图仍不参与参数求导，后续仍使用完整隐式 $J/J^*$。

源码把所声明半径的 binary64 十六进制值纳入完整表示模型的 `root_branch_radius_hex`，把整个 policy 写入 `working_evaluation.endpoint_root_policy`。因此扩大搜索域必须得到新的、由实际运行计算的 policy/model 身份，不能沿用本次 `0595aab4…` 身份。

R695 是有明确前提的统一收缩/隐式函数论证。这里从未验得其全域常数，也没有把默认 $1/2$ 当成该定理已经认证的球。因此保留有限球而改变其显式数值半径，不是在放松已通过的 IFT 证明，也不改变本课题的完成标准。任何后续完整连续根证书仍须对实际新表示单独支付全角覆盖、局部唯一性、分支拼接及数值根对应责任。

## 3. 下一次只改变一个科学输入

下一次输入选择为

$$
r_{\rm search}: \frac12 \longmapsto \frac34.
$$

选择依据仅为这次真实失败批的最大修正已非常接近声明搜索边界；这支持测试是否需要更多搜索空间。它不证明边界是唯一失败原因，也不证明较大球内存在、唯一或能找到根。若这次仍失败，失败仍正常返回，不能以零根代替。

以下内容全部保持：

- 两个精确宽支撑三元组为 `(1/32,1/4,15/32)` 与 `(17/32,3/4,31/32)`。
- 准确固定目标、实际参考四项输入、原自由变量初值与字面零根种子。
- `2e-12` 残差验收、`24` 次 Newton 预算、`18` 次回溯、`1e-4` Armijo。
- 全部 core、共享五次 omega 和 $H$ 自由量，完整母范数、原不等式前缀、全真实几何与幅度筛选。
- 同一数值积分阶、全角/径向观测、永久位置及其地址语义；不转移旧场连续证书。
- 五个完整科学/reader 源字节。

| 文件 | 未改变的 SHA256 |
|---|---|
| `so3_zero_closure_endpoint_operator.py` | `5b4c3921a0f56a9ac3acc12c03e788b3b648b15817b2e89e155a18feb2b24c46` |
| `so3_zero_closure_geometry.py` | `7698fd89e1b739391e2139c6c88dacd0c3b3d8be614fd65e435508420326b385` |
| `fullclosed_zero_closure_so3_qp.py` | `b4d71ade8082d99dfef6eefc0e26aed83eeda507aa2e9656864bf2c596977d4b` |
| `launch_zero_closure_so3_actions.py` | `27414140270a0fb1a9533a21a0bd28a46988c55aecd9952c38e7c05512b64166` |
| `read_zero_closure_so3_report.py` | `b25e5a5f370e69fe8164d835a608b1845db926d2488939dc9bafaa3bba0a6857` |

## 4. 完整可执行两阶段参数与边界

完整参数文件 [resume-20261126-zero-closure-wide-radius075-steps.json](../computations/resume-20261126-zero-closure-wide-radius075-steps.json) 为 `18550` 字节，SHA256：

`7650cd9dd8bd4390486484c049219f92902e7def075f476b727b6b5ebf28d187`。

新输出目录是 `zero-closure-axisymmetric-so3-wide-support-radius075-first`。两个步骤标识分别为：

- `complete-independent-zero-closure-SO3-wide-support-radius075-first-20261126-recover03b`；
- `actual-independent-zero-closure-SO3-wide-support-radius075-first-attribution-20261126-recover03b`。

该文件从上一完整 wide ready 逐项复制，静态核对排除地址与标识后唯一科学 argv 差异为 `--endpoint-root-branch-radius .5` 改成 `.75`。同源五文件均重新核字节 SHA256；没有本地执行科学计算。summary 增加真实 policy 的五个标量叶子，便于公开归因，而不更改报告生成或科学验收。

纯 reader 的 parent 仍是已经存在的实际参考 `reference.npz`；初根失败时不会因为不存在 `final.npz` 而遮蔽真实失败。完整末态核对仅在实际报告声明完整 final 后执行。未来表示身份和科学结果保留 `null`，等待真实 Actions 返回。
