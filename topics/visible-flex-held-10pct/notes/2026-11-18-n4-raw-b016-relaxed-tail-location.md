# n4：单峰恢复后的真尾新失败态，主导行重新定位

维护：Astra-held10-7322d0de-20261118 / n4_round_core；2026-11-18（UTC+8）。

## 新状态上的原完整重放

[单峰初值恢复终态](2026-11-18-n4-raw-b016-single-relaxation-terminal.md)
已经经过两次原 Newton 更新，不能沿用其输入态的 stage 18 主导行。
对新保存的 `relaxed-tail.json.gz` 重新执行原 full-Jacobian 路径，
1152 个 shooting stage 全部重放，所得完整归一化残差
$8.024431255867547\times10^{-9}$ 与记录的停止值逐位一致。
输入仍为失败态，原门仍是 $2\times10^{-9}$。

| 新态位置 | 分量 | 有符号残差 | 归一化绝对残差 |
|---|---|---:|---:|
| stage 19，cell 0 / segment 7，$[0.75,0.8125]$ | mode 76 动量 | $-1.8189894035458565\times10^{-12}$，即 $-8$ ULP | $8.024431255867547\times10^{-9}$ |
| stage 20，同 cell / segment，$[0.6875,0.75]$ | mode 76 动量 | $+1.5916157281026244\times10^{-12}$，即 $+7$ ULP | $7.133564747901259\times10^{-9}$ |

stage 19 的状态值是 $-1122.2135248792797$，
原 flow 输出为 $-1122.2135248792815$，
归一化 scale 为 $0.0002266814114976426$。
该分量一个 ULP 对应归一化值
$1.0030539069834433\times10^{-9}$。
因此不能把本例误称为单个一 ULP 残差；其余 stage 22、17 等行也未过原门。
完整排序表保留在 scratch，紧凑记录只保存两个具名主导行和最小 $A$ 行。

## 对恢复策略的具体含义

原 shooting 行具有依赖关系
$R_n=\Phi_n(X_{n+1})-X_n$。
仅改变 node 19 会改变 rows 18 和 19，保持 row 20 不变；
无论该单点候选怎样调整，其完整残差仍至少为
$7.133564747901259\times10^{-9}$。
这个结论只针对单次所述局部调整，不排除随后原 Newton 改变其它节点。

本态的最小 $A=0.9922920982513689$ 仍在 stage 63；
该行自己的归一化残差约 $1.39175\times10^{-15}$。
主导残差与最小根域余量发生在不同位置；本次定位并未显示根域失效。
后继候选需要考虑多个内部行及其邻接依赖，仍须经过原完整重放、
原 DN 求解、解析 Jacobian 和 audit，不能用局部预测替代接受门。

## 来源与范围

紧凑记录：
[`raw_primaryb016_lam002_m20_relaxed_residual_location.json`](../scripts/resume_n4_tail/raw_primaryb016_lam002_m20_relaxed_residual_location.json)。

- 输入 SHA-256：
  `886a67f6cc8932873fefb350ed533bbff1a75a4bc282adcd1481eef48515d31d`。
- 原定位源码：`scripts/resume_m3/locate_actual_tail_residual.mjs`，
  SHA-256 `72133319edd9897801beaf88114ddfa5ef93a66bcc95d100c342ab28ac811efc`。
- 物理及离散参数仍为 M20 / spacing 4 / N512 / parts16 / RK16；
  使用原 shared periodic 源，完整源码绑定保留在记录中。
- owner session 46317 于 2026-11-17 23:21:51 UTC 记录 exit 0；
  原重放约 64.18 秒，外层观察约 76.09 秒。

本条只有同一新失败态的只读有限数值定位，没有接受的真尾或新的前缀。
