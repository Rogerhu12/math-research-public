# R150：四个原值的 native 六列实际返回与完整 V 基量的分母范围中止

日期：2026-11-28（Asia/Taipei）。Astra-ISP-8542378f-20261127。

**准确状态：首次执行不是资源超时。** 十二条真实 $\lambda,T$ 乘法关系和 $q_{T4},R_6,N_{\rm low},P_{\rm low}$ 四个原值的纯权六列来源已返回。随后在完整 $N_4(V_0),N_4(V_0,V_1),N_4(V_1)$ 基量循环中，旧 native reducer 的分母支持断言失败，内层 exit1。没有新 $\alpha,\chi$ 原值行、完整五值结果或新 cofactor 返回，不宣称 W 排空。

## 1. 冻结实际身份

源：[2026-11-28-unit211-W-alpha-chi-native-first-five-original-values-8542.py](2026-11-28-unit211-W-alpha-chi-native-first-five-original-values-8542.py)。

- Git blob17703ecbfb46246c5f36fd4dda25626cf83f4043；13648 B。
- SHA256：71d5dd5050a034a053bacd6d390cac9cabdbb845370f795f9c7731f2aa845235。
- run46119359308 / job140900220947，内层 exit1。
- 驱动54.698322283秒，RSS201164 KiB；预算180秒/4GiB，未触资源边界。
- stdout2772 B，SHA256：913234efc4f6bd27cb829452b433a99336a3d9f6caae4a5fa703dd7a86cddac9。
- 源提交及真实pull均为1ec3af1e364131e0359272a24ea7d3713d2af369；2026-11-28 07:02:50.702983 UTC，两README无变。

源与失败身份冻结；不删除断言，不重启本门，不提高预算。

## 2. 已完成的数学范围

在当前原 W 图上令

$$
b=(1,x,y,t,y^2,yt)^{\mathsf T},\qquad
F=(E_1,E_{B,e},E_{B,o},N_1,NS,PS).
$$

对 $\theta=\lambda,T$，已逐个实际返回六条

$$
M_{\theta,j}b-\theta b_j=E_{\theta,j}F.
$$

后两来源系数为零；这里所有右侧来自四条真实原二次，而不是自由六维上的矩阵假设。后续固定先 T 后 $\lambda$ 的动作以

$$
r_{\theta v}=r_vM_\theta,\qquad
\tau_{\theta v}=r_vE_\theta+\theta\tau_v
$$

维护 $r_vb-P_v=\tau_vF$ 的完整来源 DAG。未把两个矩阵假定为自由空间上的交换算子。

在此基础上，四个原多项式已经形成纯权六行，且所有系数分母经当前已付权表检查：

| 原输入 | 完成秒数 | 六行定义字节数 | SHA256 |
|---|---:|---:|---|
| $\lambda$ 六条动作 | 16.045909146 | 166833 | 15e2c02c9ab840740931ca57343c6066bf28e73949e25a3b8b72c1fe7f4f6749 |
| $T$ 六条动作 | 16.732030934 | 170801 | 1db3d379ce733e49fdcc0706f2809cbbfd1e137d1770dc349dfcece10860dea5 |
| $q_{T4}$ | 18.493650553 | 598491 | 6795e5af591003890858b4f9bad47c8c79a51f2f4ca283205b6932e299c2249e |
| $R_6$ | 41.016395757 | 2884050 | 162adf45a040131d0e3969927dbeabfab4278dcf3bbc93ef79f8c75ec7cffb03 |
| $N_{\rm low}$ | 46.750010903 | 1466197 | 1a3a59261a5fcca94f7e20d3706f83c5e89c5bd7d47e3449a1b12dcdea29da9a |
| $P_{\rm low}$ | 52.375648366 | 1501299 | 59d7a8470e93df05d5d732a57a93ae8353e6bb15850e061d553e6506e85c09d2 |

$q_{T4}$ 的完整来源是
[C4及其已付首一四次](../results/R150-appendix-unit211-W-global-monic-T-four-F-two-and-finite-original-environments.md)第1–2节；C4本身在[同值两原四次](../results/R150-appendix-unit211-W-original-two-quartic-necessary-values.md)式(9)中有完整原组合。其余三个式遵循[低D次原理想压缩](../results/R150-appendix-unit211-W-original-odd-NP-full-NV-lower-D-ideal-compression.md)。

这些数值是可再生定义的规模与哈希，不保存大系数或展开来源乘子。完整原来源由固定源码、已返十二条动作和源 DAG 定义；不把最终大乘子称为已经展开。

## 3. 确切失败位置与未完成范围

Traceback 指向新源第209行的 add_base 调用，再指向原 C9 源 reduce_six 第334行：

    for cf in row:
        assert strip_known(cf.d,full_chart_units)[0].total_degree()==0

这是旧 reducer 的分母支持检查。该调用中，第331行的六基元余式检查和第332行完整原 trace 检查已经先于它执行。它不是原理想单位返回，也不是某个原方程的反例。

日志没有输出该循环的具体 Z 标签或失败分母，故不猜是哪一条 Z 的实际索引，也不填写不存在的系数哈希。

静态源比较解释了输入范围的不匹配：旧 full_chart_units 仅包括当时原权、$k+1$、旧 $H$、所选二次头与 C9；完整值向量

$$
V_0=(1,\lambda-1-T,1+T/\ell,1+T/\ell),\quad
V_1=(0,0,m/\ell-\rho,m/\ell+\rho)
$$

额外含 $\ell^{-1}$。当前顶层已经引用整 $\ell=0$ 排除支付 $\ell$，但这个付款没有进入旧 reducer 的固定支持表。除了原旧支持，这些基量新引入的分母支持只可能来自 $\ell$；这是符号来源分析，不是声称日志已经打印了某个失败因子。

本次未达到以下阶段：

- 三个完整 V 基量的统一完成标记及 $V_{\rm low}$ 六行；
- 任何新原值的末次 $\alpha,\chi$ 两列返回；
- 五个原值的完整 I11 新接口；
- 两个新原值 pair、任何新参数覆盖或排空。

原先 a96d 完整 I6 十行及三个标量的成功不受此中止影响。

## 4. 后继的边界

旧 reducer 和本次失败源保持不动。后继可使用新整值向量

$$
\widetilde V_0=\ell V_0,\qquad
\widetilde V_1=\ell V_1.
$$

原 N4 对向量齐次二次，故三基量可先对无 $\ell$ 分母的两个原向量归约，再在当前明确支付 $\ell$ 的权环中乘 $\ell^{-2}$。这保留完整 N4(V)，不绕过旧断言，也不增加新的几何单位。

后继只接实际未返回的原值和末次坐标目标；已有四个六行不作为附加复验门。本页没有宣称后继已经执行。

[小回执](2026-11-28-unit211-W-alpha-chi-native-first-five-original-values-first-execution-8542.json)保存全部实际 checkpoint、原退出及准确未完成范围。
