# R927 原两端参考极点铅笔的完整局部理想与范数帧：执行契约

## 1. 本次计算的唯一对象

本消费者执行 [R927 原证明](../results/R927-original-endpoint-pencil-content-and-complete-norm-frames.md) 第6–7、10节的**参考铅笔**分支。固定原辅助素数
$\ell=1000000753$、$\zeta=549966761$、$s=99932770$，固定原两个端点
$P_0,P_1$、源参数
$\rho_0=z-z_0$ 与 $\rho_1=\iota^*\rho_0$。

原 R879 已完成
$$
v_0=f/u=-g/b,\qquad ug+bf=0,\qquad (v_0)_\infty=254P_0.
$$
本次只在已完成 R917 两端完整秩8正规阶、已完成 R923 原目标正常函数坐标中评价这四个固定函数，计算原参考分式理想
$(1,q^*v_0)$、九个参考截面的相对坐标，以及同一原参考生成元的两端范数首项。全部新增数值在上述真实辅助地方。

本次没有五目标输入。配置中
future_target_sources={"R903":null,"R907":null} 固定进入身份，不从表达式或尚未完成的来源补造值。五目标 $\operatorname{Nm}(q^*\Phi_j)\det U_j$、原两端五目标标定、Picard inactive、指定 theta/Poincaré、非 $p$ 项或高度均不在本次完成旗标内。首 scope 不改变已发布 R907 的任务范围。

## 2. 数学源码、命令与身份

主核为 scripts/R927_original_two_endpoint_reference_norm_frames.py，新 result 为
R927-original-two-endpoint-reference-ideal-and-norm-frames，终证书为
p41-original-two-endpoint-reference-norm-frames-certificate.json。

公开 Actions 中的 CLI 是：

~~~text
python R927_original_two_endpoint_reference_norm_frames.py \
  --config public-actions-expanded-job.json \
  --out OUTPUT \
  --budget-minutes 300
~~~

核仅按 SHA 导入已冻结
R917_endpoint_order_arithmetic.py
（SHA256
c728c8e06cef3dfbe4d33f3a988cbbc1c3012909d67b4684d941effdec67033d）
的有限精度多项式及完整阶算术。新 result、源码、stage 前缀与 tag 均独立；不修改被导入模块的全局身份，也不运行旧 R917 正规化或 R923 目标坐标求解。固定 python-flint==0.9.0。

新 tag 包含主核/算术模块/本契约的真实 SHA、R927/R912/R923/R879/R876/R872 六原证明 SHA、原地方与完整策略常量，以及五组原来源的 BASE 五字段、原配置指纹、实际选入文件完整 SHA 指纹和原终证书。所有实际数学输入逐 plain spec 和 source group 写入 tag。目录、Range 路由、运行预算、workflow 运输时间不改变数学身份。

主入口直接要求原公开仓库 Actions 环境，设置 Python 整数字符串上限为0。包装器只执行标准库 IO、schema、SHA 与布尔出口检查；不导入数学核或在核外复算有限域等式。

## 3. 五组真实原来源

各组保留原 result、source、configuration 和成员字节。当前活动来源为：

| 组 | 原 run | 本次读取 |
|---|---:|---|
| R923 | 43915625047 | 真 FINAL；两端各 certificate、target operators、17个正常坐标块和完整272方程证书 |
| R917 | 43904492746 | R923 逐项引用的两端原 complete-order certificate、完整 order 和原 primitive/t/dual7/nu 帧 |
| R914 | 43898224893 | 原 $P_0$ 的273×146正常函数 jets及原 $P_1$ 点/零阶运输检查 |
| R879 | 43835253379 | 原 reference-function-and-pencil、unit-solution、source audit 与真 FINAL |
| R872 | 43830071469 | 原 u、已接受 b 小叶、fixed-chi 小证书与 source audit / FINAL |

每组还包含原 public-actions-input.json、run-receipt.json、
core-receipt.json、完整 manifest。包内原 manifest 只负责绑定原成员；其未选入的大载体与旧矩阵不因此成为新需求。

R923 的实际原输入精度是两端各267项。本核记录该实际精度，再取工作精度
$N=\min(9,N_{\mathrm{target}},N_{\mathrm{order}},N_U)$。
九项截取只为新的参考首项；不把267改称本次重算，也不把尚未使用的高阶丢失误称源不足。

R879 原函数文件已保存准确 unit-solve 的定义、$f,g,u$ 的三行272正常多项式、原 $V_2$ 基序、原 $U_{272}\ne0$ 与18阶分子首项。R872 的小 b 叶按相同原 $V_2$ 序恢复。旧418核与272阶 Hensel jets不重新计算。R914 的矩阵直接是原 $e_i/\tau$ 函数展开；原 $82^2$ 整数尺度已经包含，不再乘除一次。

纯 IO 包装器从真实原平台 archive 通过 Range 取所需原成员，逐 bytes/SHA 与完整 manifest 校验。Range 请求不冒称已经全量重哈希原 ZIP。新 carrier 只打包本次实际选件和原元数据，原成员的数学标签不变。实际选件数只在完成取源后记录，不按计划预填。

## 4. 完整原目标函数与两个主分量

在每端取 R923 的 normal_values_in_original_endpoint_order_mod_prime
和原目标 $U$，以原三行正常多项式评价 $f,g,u,b$。先保存全部8个坐标的
$ug+bf=0$ 乘回。这里只新评价这四个函数，不重建任何旧函数系数或目标正常基。

目标 $P_0$ 的极大理想由
$$
q^*(z-z_0),\qquad
q^*(\beta_i-\beta_i(P_0)),\quad 1\le i\le144
$$
生成。$z_0$ 从原 V1 零阶行
$e_1/\tau=z-\beta_{72}$ 和 $e_{73}/\tau=\beta_{72}$
恢复；不把双重坐标关系再变换一次。原 R805/R914 源保证其余 degree2 正常行是原 V1 乘积，故这些是真完整环生成元。

在完整8维剩余代数内实际保存 $I,I^2,\ldots,I^8$、全部乘积列与核：
$$
A_{P_0}=\operatorname{Ann}(I^8),\qquad
A=A_{P_0}\oplus I^8.
$$
保存真实秩 $r$、全8换基/逆、两幂等元与全部乘回。幂等元用
$e\mapsto3e^2-2e^3$ 提升至 $N$ 项，之后在同一完整8维阶中保存两块换基与两侧逆。全部因子、分歧和幂零元保留；不拆闭点、不开平方自由商，也不把2+3+3的支长度改成3个标量值。

若实际 $r=0$，目标 $P_0$ 块严格为空；其范数为1、阶为0。这是合法实际分支。若补块秩为0，同样按空块单位和范数1处理。

## 5. 最多九项的原参考范数首项

在 $P_0$ 完整块上计算目标参数 $q^*\rho_0=q^*(z-z_0)$ 的整个乘法矩阵行列式。必须实际看见
$$
N(q^*\rho_0)=c^*\rho_\epsilon^m+\cdots.
$$
非空块时 $1\le m\le8$，空块时 $(m,c^*)=(0,1)$。上界来自原目标映射次数8，故九项足够。少于九项而未见首项时保存真实 NeedPrecision；九项仍与已证上界矛盾则作为实际断言失败记录，不能伪称成功或零函数。

原 R879 的准确首项
$f=\rho_0^{18}(1+\cdots)$、
$u=U_{272}\rho_0^{272}(1+\cdots)$
给出对非零整数 $\lambda$：
$$
N(1+\lambda q^*v_0)_{\!P_0}
\sim
\lambda^rU_{272}^{-r}(c^*)^{-254}
\rho_\epsilon^{-254m}.
$$
这里只利用既成准确18、272、254阶；不会新增一个局部272阶求值任务。

补块中原 $(u,b)$ 是单位理想。依次实际检查 $\eta=0,\ldots,8$，取完整乘法矩阵
$M_u+\eta M_b$ 的模 $\rho$ 行列式非零者，保存其真完整单位逆及
$$
M_{v_0}=(M_u+\eta M_b)^{-1}(M_f-\eta M_g).
$$
完整左右商乘回和全部因子都须保留。使用整个补块的特征多项式构造
$C_\epsilon(T)=\det(I+TM_{v_0})\bmod\rho$，保存完整 Cayley–Hamilton 乘回；不逆任何非单位。

## 6. 两端共用的参考生成元与九坐标

每端保存非零选择多项式
$$
d_\epsilon(T)=T^{r_\epsilon}C_\epsilon(T),\qquad \deg d_\epsilon\le8.
$$
扫描同一整数 $\lambda_0=0,\ldots,16$，只接受两个实际值都非零者。有限域特征大于16且两个非零多项式总次数不超过16，故有合法选择。任何非空 $P_0$ 块会自动排除 $\lambda_0=0$；两个块都空时保留其合法性。

保存整个原8维基中的两相对乘法矩阵：
$$
C_0=(1+\lambda_0q^*v_0)^{-1},\qquad
C_1=q^*v_0(1+\lambda_0q^*v_0)^{-1}\pmod\rho.
$$
在非空 $P_0$ 块上它们分别为 $0$ 和 $\lambda_0^{-1}I$；原254阶和原分歧界给 $\rho$ 阶至少84，故该断言作用于完整幂零块。补块使用上节真单位逆。保存
$C_0+\lambda_0C_1=I_8$ 全64项，以及
$\det(C_0+iC_1)=d_\epsilon(i)/d_\epsilon(\lambda_0)$
九个完整秩8行列式检查。

九坐标只是相对坐标。原参考分式格另外保留准确表达式
$$
(1,q^*v_0)=(1+\lambda_0q^*v_0)B_\epsilon,\qquad
\det U_{0,\epsilon}
 =\frac{N(q^*(u+\lambda_0f))}{N(q^*u)}.
$$
不展开巨大 Laurent 格，也不丢弃分母 $N(q^*u)$。

## 7. 原 $\rho$、$t$、dual7 与参考 determinant 帧

完整范数阶与首项是
$$
m_{0,\epsilon}=-254m_\epsilon,\qquad
L^\rho_{0,\epsilon}
 =\lambda_0^{r_\epsilon}U_{272}^{-r_\epsilon}
 (c_\epsilon^*)^{-254}C_\epsilon(\lambda_0).
$$
从 R917 原帧读取真正 $c_\epsilon=(t_\epsilon/\rho_\epsilon)(P_\epsilon)$；
核对 $c_1=-c_0$，但不把两端原参数改成同一参数。原 $t$ 首项是
$c_\epsilon^{-m_{0,\epsilon}}L^\rho_{0,\epsilon}$。

保存两端同一全局参考生成元、原 R879 t 帧定义、原 dual7 的
Nm_pi_t(pi_s^*I) 方向、两个 determinant 因子、原 $\nu$ 与
$\iota^*\nu=\nu$。最后记录实际 $t$ 首项的 $P_1/P_0$ 比值。该比值是本参考帧的值，不冒充五目标标定或指定 theta/Poincaré period。

## 8. 原子恢复与诚实终点

所有新数学 stage 位于输出根目录，前缀 R927-reference-、类型 .json.gz。
每个完成 stage 同时写 complete=true 与同一完整 configuration。
当前断点为 R927-reference-current.json.gz、complete=false。
stage manifest 列出所有实际完成数学 stage，排除自身与当前断点。

每端的函数评价、理想幂/annihilator、幂等元/换基、完整块矩阵、参数范数、补块单位、prepared endpoint 分别原子保存。两个端点独立记录 NeedPrecision，另一端仍可继续。两端 prepared 都成后才选择同一个 $\lambda_0$，再保存两端终证书和参考帧比值。

恢复只复制同源码/同数学 tag 的已完成 stage 与实际 current。
历史 complete=false FINAL 不约束更新后的 current SHA，也不作为完成缓存。
只有真实成功 FINAL 才要求完整 inventory/current/所有引用一致。
预算停、异常或 outer timeout 均保原子成果与真实 run/core receipt；
若 outer timeout 尚无 core receipt，包装器如实记录 null。

complete=true 当且仅当两个原参考局部理想、全8维相对坐标、完整参考范数首项与同一全局生成元的原 t 帧比值全部完成。局部真实完成不转换成五目标、高度或 Picard 判定。核与包装器分别输出精确阶段数、原选件数、实际分块秩/阶/参数/首项和原源 SHA，禁止按请求预填这些数。

全部新数学只在公开 Actions 运行。源码解析与原来源 IO 属于同一次真实运行的必要步骤，不新增独立测试或审核门。
