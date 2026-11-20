# R138 补篇：真实根锚定的完整局部漂移预算

2026-11-20，visible-exact-astra-ac637-20261120。

**结论。** 公开 [run44762838206/1](https://github.com/Rogerhu12/math-research-public/actions/runs/44762838206)
已经完成同一实际 Qrepair 上的两个新标量。完整保存球严格给

$$
D_{loc}<\frac{3}{4000},\qquad
\Gamma_{loc}<\frac{1001}{1000}<\frac{101}{100},\qquad
\sqrt{\Gamma_{loc}}<\frac{2001}{2000}.
\tag{RDA.1}
$$

这里 $D_{loc}$ 是本算法选定的完整漂移导数积分上界，
$\Gamma_{loc}$ 是保存、读回该上界后形成并再次保存的指数上界。
这些数值不是实际漂移大小的下界，也不是正区边界问题的逆常数。

## 1. 原对象和这次真正新增的范围

数学依据为 [RA 的真实根初值与完整容量接收器](R138-supplement-root-anchored-local-drift-and-capacity.md)，
运行入口为[两标量合同](../notes/2026-11-20-R138-root-anchored-local-drift-contract.md)
和[准确输入清单](../notes/2026-11-20-R138-root-anchored-local-drift-inputs.json)。
候选仍为 `ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413`，
连续修补定义仍为 `440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47`。
固定 $\eta_0,\nu_0,\alpha$、完整 moving mean、真正 physical $\Theta$ 和全部原接口未改变。

原 moving 漂移满足

$$
d=-\beta I_\phi(u^2+Kv^2),\qquad
d_\phi=-\beta\Pi_0(u^2+Kv^2).
\tag{RDA.2}
$$

新目标是原真实根层 $[r_*,r_*+1/100]$。实际积分以非负包围覆盖

$$
\left[\frac{1191984371497}{5000000000000},
       \frac{2483968743003}{10000000000000}\right],
\tag{RDA.3}
$$

包含一个完整原 germ 片和326个原 positive 交片，共327片。
整个原4650行和3594个接口均在准入时保留；未把根中点或区间端点当作真实初值。
新分区 hash 为 `bb8770fda129870ef3c7e143ceb93f499a155827b51a949c8be9cc6bcb17a2fc`。

每片直接消费原整行的 Wiener 上界，保留完整 pair 修补
$\|e_u\|_{A_0}+\|e_v\|_{A_0}\le4\cdot10^{-18}$。
没有缩小原系数包围、重新求 Fourier 系数、扫描旧 angular 缺陷或积分任何 flow。
只恢复原 positive4 和 germ1 五件历史字节；旧 X 的完整全域积分与指数直接只读。

## 2. 两个完整保存记录

[实际科学结果](../notes/root_anchored_local_drift_ci/run-44762838206-1/root-anchored-local-drift.json)
的两条 `complete_decimal_ball_v1` 记录如下；每行表示
$(M\pm R)10^e$ 的整个保存球，方向均为 upper。

| 目标 | $M$ | $R$ | $e$ |
|---|---|---|---|
| `complete_drift_integral` | 74790380247915852257788687565167028632458102753950070749807494445132638478769719 | 2 | −83 |
| `complete_local_Gamma` | 10007481835522656693652353311383312152700151913515754541955820253303112416485026 | 2 | −79 |

十进制展示分别约为 $0.0007479038024791585$ 和 $1.000748183552265669$；
所有比较使用上述整球，不使用展示小数。
完整积分保存并读回后才取指数；指数保存并读回后才判门。
327片全部完成、`saved_record_count=2`、`complete=proved=true`，无失败。

预先声明的 $\Gamma_{loc}<101/100$ 比较为 true。
新保存 upper 严格小于原 X 保存 `Gamma` 的 lower 的比较也为 true。
后者仅比较两个已选预算数值，不声称原 flow 的最优 Jacobian 有该下界。
(RDA.1)的更宽有理比较直接由保存整数给出；最后一项还用
$1001/1000<(2001/2000)^2$，不是一个新的科学目标。

## 3. 完整输入、输出和实际执行

| 对象 | bytes | SHA256 |
|---|---:|---|
| 新科学源 | 19541 | `9c468c51dfe5b2e6e4406ea39621bcf8a1d74b51afc4c740a00039e8a436b915` |
| worker | 32390 | `c64a47926f60c69fb1054d2fca46ffe8d7f7f01ffbbf2ab5836a0ee220690177` |
| metadata generator | 10873 | `03046560e9ce60cd995e795ef9cd6954ee404482463a054b67c6621fbc06473e` |
| manifest | 8972 | `e8dfa5e0022ee9c0805e5afbbdbecd0f8af37239b2c71d3d7cdedd5665dda4cf` |
| actual | 8061 | `c6b9e8a018443183c72560ce48441b02399f9644eb73fd009913a1ce52ca78c2` |
| execution | 12186 | `7e6da01a3879e7774028c47a5c9a29ac5b72a6ce1fb91da77372ec05c9746160` |

实际科学 checkout 是 `508361deeced8b55bb35c5c2ed004edf2450fb94`。
15个当前输入收据逐项等于 manifest；五件原历史 bytes/SHA/blob 与清单逐项一致。
原 positive/germ 的完整 native SHA 分别仍为
`ea17451120f8c368ea3e5d4ee511a9d1d03d8a97705e7bd36cf9d015a8d9d93d` 和
`397f9b428c787823994f8c849ad7d1f9209220c3c6e8907b38be562b3cbc9864`。

[执行收据](../notes/root_anchored_local_drift_ci/run-44762838206-1/execution.json)
记录320bits、单 child、返回码0、数学时间0.1966190449999914秒、child时间0.8732309439999995秒。
全部旧目标、新 flow、新 capacity ODE及新数组计数为0。
worker记录五次实际 pull/README 核查；保留的首个和末三个完整收据均为空差异，
读点仍为 `96edc677044b6ad7c7fd3aa2f65bf77d9c0e27a1`。
本页不另声称重建了未保留的第二个完整收据。

## 4. 现在可以使用的接收式

在此同一根层上，以真实初值 $\psi(r_*,\xi)=\xi$ 解辅助 drift，
有 $\Gamma_{loc}^{-1}\le\psi_\xi\le\Gamma_{loc}$。
RA.9 因此给出完整合法的新系数

$$
\begin{split}
\alpha_E^{root}(W)
&\le |\rho|^{-1}\left\{
\frac{2001}{2000}N_W
 (\sqrt{C_{E,\alpha}}+\sqrt{C_{H,\alpha}}h_E)
 +P_{W,1/3}\sqrt{A_\Theta}\,r_E\right\},\\
\alpha_B^{root}(W)
&\le |\rho|^{-1}\left\{
\frac{2001}{2000}N_W\sqrt{C_{H,\alpha}}h_B
 +P_{W,1/3}\sqrt{A_\Theta}\,r_B\right\}.
\end{split}
\tag{RDA.4}
$$

这里 $N_W$ 仍必须在同一个真根层、同一径向权和同一完整接收器上实际支付。
physical $\Theta$、$P$ 的 mean、原 $r_E,r_B$、$Q_H$ 全尾和真实 $D_H^{-1}$
均未免除。根初值改变只省去了根行的另一遍 density 转授；能量 Jacobian 仍在。
全域 body 可另用原外端初值 flow，但不把两个辅助函数等同。

原 GB 下整类径向权接收器已被 RS 排除的结论不变。
将本页同新谱体预算或更完整的可达迹约束组合，仍需各自的实际常数和严格门。
本页不授 finite capacity Gram、根负部、正区全逆、非线性 core 或最终闭等距族。
