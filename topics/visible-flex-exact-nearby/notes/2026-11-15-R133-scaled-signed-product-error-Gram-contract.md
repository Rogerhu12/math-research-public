# R133：同一 Poisson 乘积的有向误差 Gram 与准确缩放 dyadic

本节只改变既有完整 $97$ 输入 Poisson 乘积的误差包围和正权编码。
原 $5970$ 个同 $F$ 矩阵、原两端边界、完整均值、实际 $V$ 跳及
$7908$ 格帽伴随 Gram 均保持原身份。本节不授完整无限维逆，
也不预授新公开运行成功。

## 1. 实际失败及须重做的临时算术

公开运行 $43681612825/1$ 的数学子进程在
2026-11-15 07:05:06 UTC 实际返回 $1$。原 stdout 为 $70333$ bytes，
SHA256 为
69181f59587aec5db8d0d135f4ede675a7b7610c2b3bfd0470228951981e7750。
零数学收据运行 $43689244062/1$ 先核定其大小及 SHA，
随后才读取这个小于 $100$ KB 的原 UTF-8 日志。

完整调用链是旧 v2 science 的 merge_group 第 $315$ 行，
原 complete97_right_Poisson_Grams.weighted_add 第 $72$ 行，
再到原 same_F_triangular_source_Gram_pilot.exact_upper_float
第 $65$ 行。前一函数已检查 Gram 范数上端有限且非负；
失败发生于其平方根转成 binary64。因此证据是
**有限正 Arb 上界超出 binary64 可表示范围**，
不是出版故障或已经验证的全局 Gram。
单凭堆栈不能证明唯一放大机制必定来自某一个误差项。

实际小结 actual-conclusion-summary.json 的 SHA256 为
770a61fa89902954178cf1a2bb9a347312232545e434685f9e332a2ce149b8db。
最终逐完整文件计数优先于每 $16$ 格一次的进度显示：

| 临时阶段 | 完整文件数 | 原已持久成功记录 | 本次未持久化的新算术 |
| --- | ---: | ---: | ---: |
| future | 4226 | 1886 | 2340 |
| past | 1800 | 0 | 1800 |
| product | 4331 | 0 | 4331 |
| canonical ports | 5970 | 0 | 5970 |
| complete local groups | 0 | 0 | 0 |

根规第 $15$ 条禁止新可重算输出持久化，这些新临时文件在作业结束后
不可跨运行恢复。后继清单明确重做这些未保存算术，不能称为零重算。
原 $1886$ 条 future、原完整 $F/C$、源与输出 Gram、候选、
target 和 validator 则仍逐字节复用，零旧数学重跑。

## 2. 同一个准确乘积与完整误差恒等式

记原闭合坐标事件的准确逆块为 $D_i$，它由原完整区间矩阵包围，
不是所选中点。真正未归一化 Poisson 乘积为

$$
E_{-1}=I_{97},\qquad E_i=D_iE_{i-1}.                 \tag{G.1}
$$

令 $\widehat E_i$ 为新选择的准确缩放 dyadic 矩阵，定义

$$
\Delta_i=E_i-\widehat E_i,\qquad
W_i\succeq\Delta_i\Delta_i^*,\qquad W_{-1}=0.         \tag{G.2}
$$

每步对包含同一准确 $D_i$ 的整个区间矩阵计算
$D_i\widehat E_{i-1}$，完整中心差给出

$$
R_i=D_i\widehat E_{i-1}-\widehat E_i,\qquad
\|R_i\|\le r_i,\qquad
\Delta_i=D_i\Delta_{i-1}+R_i.                       \tag{G.3}
$$

$r_i$ 包含原 $D_i$ 区间半径、矩阵乘法舍入及新中心选择误差，
不能只用 $D_i$ 中点或只付新的 binary64 舍入。

对任何准确正 dyadic $\eta_i>0$，正权 Cauchy 给出

$$
W_i=
(1+\eta_i)D_iW_{i-1}D_i^*
 +(1+\eta_i^{-1})r_i^2I_{97}
 \succeq\Delta_i\Delta_i^*.                         \tag{G.4}
$$

先保完整 signed 矩阵乘积，再作 Loewner 上包围。
$D_i$、旧误差和 $R_i$ 可以相关；(G.4) 不使用独立性。
$r_i=0$ 时只用准确的传播项；
$D_iW_{i-1}D_i^*=0$ 时只用 $r_i^2I$。

正权可取 $r_i/\sqrt{\|D_iW_{i-1}D_i^*\|}$ 的正 dyadic 上包围。
这只影响上界大小，不是新数学前提。与旧逐步标量
$\|D_i\|e_{i-1}+r_i$ 相比，(G.4) 保留误差方向。
新运行可记录旧标量递推的指数作诊断；
该诊断不进入新的证明上界。

## 3. 完整 signed 源 Gram 的消费

设 $J\succeq0$ 为原局部输出、body defect、真实 graph jump
或 waist 残差的完整 $97$ 方向 Gram。由 (G.2)，

$$
\Delta_i^*J\Delta_i
 \preceq \operatorname{tr}(JW_i)I_{97}.             \tag{G.5}
$$

因为
$\|\sqrt J\Delta_i\|_{\rm op}^2
 \le\|\sqrt J\Delta_i\|_{\rm HS}^2
 =\operatorname{tr}(J\Delta_i\Delta_i^*)
 \le\operatorname{tr}(JW_i)$。
trace 在完整 signed 矩阵相乘后取上端，
不能逐项绝对化、丢非对角或删除 even mean。

令 $N_i$ 为该 trace 的有向上端。对任意准确 $\theta_i>0$，

$$
E_i^*JE_i
 \preceq
 (1+\theta_i)\widehat E_i^*J\widehat E_i
 +(1+\theta_i^{-1})N_i I_{97}.                      \tag{G.6}
$$

$N_i=0$ 或第一项准确为零时可使用相应单项。
真实 $V$ 跳仍逐个保留；(G.2) 的中心和 $W_i$ 是同一个
$E_i$ 的包络，不产生额外物理 state jump。

最终完整 $97$ 右边界输入仍由原同一个准确选点 $C$ 归一化。
整个 (G.6) 作 $C^*(\cdot)C$；其误差单位于是为 $C^*C$，
不能无费继续写成 $I$。原 $PC-I$、加权 even-$97$ 真边界误差、
独立 mean、真正 waist 缺陷及独立 cut trace 均照旧收费。

同一输入产生的多个 $V$ 跳继续用完整正权 Cauchy 相加。
局部组只保存 $\sum H_\ell/\alpha_\ell$ 和 $\sum\alpha_\ell$，
全组汇总后再乘总权；没有把不同跳误认为独立源。
此处所有原矩阵均在已付实反射坐标中，代码的 transpose
对应准确实伴随，不扩授未付复参数矩阵。

## 4. 缩放 dyadic 的完整 Loewner 编码

所有矩阵先检查 Arb 条目真正有限。对有限矩阵 $A$，
取准确整数 $s$ 使 $\|A\|\le2^s$，在 $2^{-s}A$ 上选择两个
binary64 数组 $H,L$，定义准确中心

$$
A_{\rm c}=2^s\bigl(\operatorname{exact}(H)
                         +\operatorname{exact}(L)\bigr).           \tag{G.7}
$$

两数组在准确 Arb 层相加，$2^s$ 不通过 float。
对对称矩阵，直接选一致上下三角并保存全 signed 上三角。
若 $\lambda$ 为

$$
\left\|2^{-s}A-\operatorname{exact}(H)
                    -\operatorname{exact}(L)\right\|               \tag{G.8}
$$

的准确非负 dyadic 上界，则

$$
A\preceq
2^s\bigl(\operatorname{exact}(H)+\operatorname{exact}(L)
                                     +\lambda I\bigr).            \tag{G.9}
$$

收据保存整数 $s$、两原数组 SHA 及
$\lambda=0$ 或 $\lambda=2^e$ 的整数指数 $e$。
恢复时准确照 (G.9) 构造，不能只缩放 slack。
旧 binary64-hex 收据仍以原读取器恢复，原字节不变。

正权也允许任意整数指数的 $2^e$。以 Arb 比较和整数二分确定
$0<v\le2^e<2v$；$v$ 为二的幂时取等号。
整个选择不经 float。显式指数资源门 $|e|\le2^{30}$ 只会真实
停止不支持的算术，不截断数学值或把无限、失败改成零。

## 5. 后继完整消费与早期实际门

新 science 在公开 runner 核定原输入、原 $1886$ future 和全部
既成矩阵后，先计算首 $32$ 个真实新 product 状态。
这些新状态留在同一次运行临时目录；product 流从第 $32$ 格
继续，不再计算此段。

早期门还用一个原完整 $97$ Gram 加单位矩阵，
以准确 $2^{4096}$、$2^{-4096}$ 重标度核新中心、slack、
正权和读回，并消费首 $32$ 步的真实 sandwich。
这是实现/编码门，不用有限测试代替 (G.1)–(G.9)，
也不以首 $32$ 步宣称全局 Poisson 界。

其余两个源通道、全部真实 $V$ 跳、完整 $5970$ 格积分、
实际 $96+97$ 边界和三个输出窗全部保留。
真实 $H_Y$ 得到后，原完整帽候选和新 same-$97$ 正权候选
均保 signed Gram 到最后的 $\operatorname{tr}(H_YW_{\rm cap})$；
新帽正权也不再把有限 Arb 目标转成 binary64。

新数组、native 及原大输入只在公开 runner 临时使用。
仅发布脚本、参数、run 身份、实际 pull/README 差异、
每阶段输出 SHA 与真实小结；不上传新数据 artifact 或 Release。
未得到实际完整成功前，不能把本合同记作全矩阵 Green、
完整 $97$ 右 Poisson 或无限维 coupled 逆已完成。
