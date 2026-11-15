# actual109：联合全相位法向门的三个有理案例

/root GPT-6 Astra Pro（AI-assisted），2026-11-15。此为公开 Actions 的实际读回结论；R280 的完整证明已独立登记。

## 实际运行与结论

[run43684128674](https://github.com/Rogerhu12/math-research-public/actions/runs/43684128674)，job132720890896，source `0dda76093a03016ae90b4d72eb1aa88a0db8ba68`，attempt1，Python3.12.14，实际 success。三例均与提交的解析预期相符，`analytic_case_failures=[]`。没有读旧 fixture，没有相位采样，没有 native/BVP/RHS/J/ODE 调用。

| 新有理案例 | 两个原单端门 | 联合门 | 保留旧门后的 OR | 联合多项式升幂系数 | π 余量 |
|---|---|---|---|---|---|
| joint-strict-extension | false / false | true | true | $[1/4,0,-1/2,0,9/4]$ | $9/4$ |
| old-endpoint-retained-when-joint-fails | true / false | false | true | $[-3,0,-6,0,-3]$ | $-3$ |
| phase-pi-equality-is-not-a-strict-pass | false / false | false | false | $[4,0,4]$ | $0$ |

三例的全相位距离门和旧 normal-chord 门均 false。第一例实际验证：两个单端全相位门分别失败时，联合平方门仍能严格支付；第二例验证：必须保留原两个门的 OR，不能用联合门替换它们；第三例在所有有限半角坐标上为正且有限实根数为0，但 π 余量恰0，因此仍正确拒绝严格全相位结论。三例联合多项式的实际有限不同实根数均0；零相位余量分别为 $1/4,-3,4$。

## 可重建身份

| 对象 | bytes | SHA-256 |
|---|---:|---|
| 实际紧凑摘要（包括末 LF） | 2820 | `e91c170aaf305b157c6948ddfc636dc98dfe49926983895439f3de05379f3c52` |
| runner 临时完整输出 | 21821 | `d7df856f8d9d48d8dd08fa9fd27b5e236f8c947b5b527fee4c359609136f45fb` |
| 实际 job log | 33533 | `3e2cae25f908c8f9e2ace02e054129d7eee01dd07e8927c2d0f79db59590b828` |

输入 JSON SHA `ce9fc96ed897d27fdcbb1a9953217225f04e38b329c382ad491a243d2ce33d6b`；request SHA `1899a66371506abb558fa166cf92f9657b1935fb3c1b45658cf2e3aa7ae60e30`。执行源 `geometry_20261115_joint_phase_normal_balls.py` 为 `c5548f28bfe56a283403a7d16e1879c1c1243d0a0bc80761586fe50e1aec1466`；原 R62 核 `root_mixed_phase_normal_balls.py` 为 `ecea0ef58aa5755270807596da5512552ac52fab27e90492fcf85fab095716c6`。root只读取原日志、提取原标量与核字节/hash，没有本地科学重算。可重算输出不存 Git 或 Release。

## 结论范围与继续工作

这是条件球数据上精确有理多项式门的实际行为，`full_surface_certified=false`、`actual_reach_certified=false`。它既没有给出真实闭面，也没有给出本课题全 t reach。R280 的有限覆盖证明仍需真实闭面及有效位置/法向包围。继续 R281 的两有理相位图与闭区间 Sturm 换门覆盖，以处理同一球对在不同相位由距离门或法向门分别支付的情况；本次三例不作为新证明审批门。
