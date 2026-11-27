# R1102 — 原 full47 全73维首全局高度的整非退化性

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。  
**状态：已证明（完整有限精确计算）。**

## 1. 结论与原对象

沿 [R1093](R1093-certified-original-Gaussian-CM-generator-and-full-MW-lattice.md)，
取原 $Y=X_{\mathrm{ns}}^+(47)$、$J=\operatorname{Jac}(Y)$，
$q=4513$、$B=q+1-T_q$、$u_4=23y_{1728}-C_\infty$，
以及真实整 Mordell–Weil 格
$$
P_0=Bu_4,\qquad M=\mathcal T_{\mathbf Z_q}P_0,\qquad
\log M=q\operatorname{Lie}(J),\qquad \operatorname{rank}M=73.
\tag{1102.1}
$$
[R1096](R1096-certified-original-CM-moving-units-and-odd-Hecke-height-basis.md)
已证 $H=T_3+T_5$ 生成最大未分歧整 Hecke 代数，
且 $a=(T_2-1)/2$ 为单位，$Bu_{16}=aP_0$。

使用 R1094 的同一整各向同性补空间和同一高度符号，定义
$$
\Gamma(T)=q^{-1}h(P_0,TaP_0),\qquad
\Gamma(T)=\operatorname{Tr}_{\mathcal T/q\,/\,\mathbf F_q}(\kappa T)\pmod q.
\tag{1102.2}
$$
本次完整读取全部73个基值，得到：

- $\gcd(\kappa,\chi_H)=1$；原全部28个剩余域块上 $\kappa$ 均非零。
- 令 $w=\kappa/a$，则 $\operatorname{Norm}(w)=2992\pmod{4513}$。
- 在原整基 $P_0,HP_0,\ldots,H^{72}P_0$ 上，
  $$
  \boxed{\det(q^{-1}h)=3972\pmod{4513}.}
  \tag{1102.3}
  $$
  因而 $q^{-1}h:M\times M\to\mathbf Z_q$ 为完美整配对，
  $h$ 在此基的行列式赋值恰为73。

28个块的分布与结论为：

| 剩余域次数 | 块数 | 本次实际非零块数 |
|---:|---:|---:|
| 1 | 16 | 16 |
| 2 | 6 | 6 |
| 3 | 4 | 4 |
| 11 | 1 | 1 |
| 22 | 1 | 1 |

这里实际检查全部块，未由第一次高度 $\Gamma(1)=818$ 或十六个一次块推断其它块。

## 2. 实际运行与旧输入的准确范围

完整成功运行是
[run45962228077](https://github.com/Rogerhu12/math-research-public/actions/runs/45962228077)，
job140382522990，source **1f38ea3074411b6ca67b21824db7c90754601ad2**。
公开 Actions 状态为 success；脚本实际用时 **1838.859061013秒**，
四核、数学预算18000秒、预留120秒。使用固定官方 SageMath10.6 镜像
`sagemath/sagemath@sha256:60dfb09e8d1399e127a0d7b62b45eef1044574bae397df51bb6ba38df5498879`。

可重现输入、完整公式和唯一消费者：

- [计算方法](../notes/2026-11-27-full-p47-complete-global-CM-height-method.md)；
- [固定请求](../notes/full-p47-complete-global-CM-height-request.json)；
- [完整消费者](../scripts/full_p47_complete_global_CM_height.py)。

固定的73个指标是 [R1101](R1101-certified-original-level47-smallest-odd-Hecke-basis.md)
已经认证的全部奇 $1\le n\le149$，删去47和141。原坐标矩阵
$C$ 的行是 $T_n$，列是 $1,H,\ldots,H^{72}$，
$\det C=3946\pmod q$。消费者仅按这些已证指标重建并核坐标证书，
没有重新搜索 Hecke 基。

本次直接消费两个已经完成的值：

1. R1100、run45955885738 的 $\Gamma(1)=818$；
2. run45961230690/job140379262278 的 $\Gamma(T_{143})=4219$。
   该次完整 worker 返回后，parent 已把值保存至失败回执；
   随后的进度输出字段重名使 job 失败。只消费实际已完成的143，
   没有把其它未完成 worker 视为完成，也没有虚构143未输出的范数哈希。

因此成功续算只执行剩余71个指标的全范数和。首个 launch
run45960073755 在 Python 启动前失败，其范围与修复记录见方法§8和请求。
这两个实现故障均不被写成完整成功；(1102.3)依据上述最后一次成功回执。

## 3. 每个基高度的完整性

[R1094](R1094-original-disjoint-CM-heights-and-first-global-intersection-functional.md)
和 R1096 已付原奇 Hecke CM 分盘的 $q$-局部高度在 $q^2\mathbf Z_q$。
对每个基指标 $n$，移动平方精确展开为三个指标
$n,nq,nq^2$，权为
$$
c_0=q^2+3q+1,\qquad c_1=-2(q+1),\qquad c_2=1.
$$
保留 $T_{q^2}$ 全非循环核。设
$$
F_q(\ell)=\frac{(\ell^{q-1}\bmod q^2)-1}{q}\pmod q.
$$
沿 $\chi_\ell(\ell)=-\log_q\ell$，它正是所需
$-\log_q(\ell)/q$ 的剩余值。

全部奇好素数交数使用
[R1097](R1097-original-level47-odd-prime-CM-intersections-and-sparse-norm-sum.md)
的两个不交2209进程及完整 $1/16$ 重数；每个正范数项精确分解，
按其唯一可能贡献的惰性奇赋值素因子乘自己的 Fermat 商。
这只是交换两个有限求和次序，没有素数大小截断。
原 $\ell\mid n$ 的准规范层和复合指标的非循环核均保留。

2处使用 [R1099](R1099-original-level47-dyadic-CM-intersections.md)
的整数与半整数 Hurwitz 格全和。
坏47使用 [R1098](R1098-original-bad47-CM-intersections-and-exact-vertical-correction.md)
的水平交数及真实垂直修正
$$
23^2\sum_{j=0}^2c_jH_{47}(nq^j)+23b_{\mathrm{moved}}(n).
$$
五维 Brandt 源沿 R1100 的原矩阵哈希、权重和 $E_4/E_{16}$ 标定重建；
全部 $H_n$ 核行和 $\sigma_1(n)$、带权自伴及与 $H_q$ 交换。
故 $b_{\mathrm{moved}}(n)$ 准确是完整 $B^2$ 的条目。

完整式是方法(CH.7)。精确最小素因子表只优化小整数分解；
超表部分用 Sage/PARI、`proof=True`，并核每次分解乘积。
每个指标的三个范数范围全部走完，才生成其返回值；
parent 还要求73个指标完整且无重复。
各完整范数流的计数、SHA及三类贡献在成功日志中，
不把可重算数组另存入仓库、artifact 或 Release。

## 4. 从73个值到完整迹泛函

记 $P=\chi_H\bmod q$，$\deg P=73$，
$\operatorname{disc}P=2650\ne0$。令 $g_n=\Gamma(T_n)$。
消费者按实际行列约定解
$$
C\gamma=g,\qquad \gamma_j=\Gamma(H^j).
\tag{1102.4}
$$
坐标源已将原 $T_1,T_2,T_3,T_5$ 与实际 Hodge 矩阵逐项核对。
Newton identities 给
$s_r=\operatorname{Tr}(H^r)$，$0\le r\le144$，
迹 Gram 为 $G=(s_{i+j})$，且实际核
$\det G=\operatorname{disc}P=2650$。
解 $G\kappa_{\mathrm{coeff}}=\gamma$ 得唯一迹乘数。

另构造
$$
R(X)=\sum_{i=0}^{72}X^i
       \sum_{j=0}^{72-i}\gamma_jp_{i+j+1},
\qquad P(X)=\sum_{i=0}^{73}p_iX^i .
$$
无穷远展开
$\operatorname{Tr}(\kappa/(z-H))=\sum_{j\ge0}\gamma_jz^{-j-1}$，
乘 $P(z)$ 取多项式部分便是 $R(z)$。
在各简单根处取留数得到
$$
\kappa=R(P')^{-1}\pmod P .
\tag{1102.5}
$$
成功回执中(1102.5)与迹 Gram 解逐系数完全相同。

最后，由 Hecke 自伴与 $Bu_{16}=aP_0$，
$$
q^{-1}h(SP_0,TP_0)=\operatorname{Tr}(\kappa a^{-1}ST)\pmod q .
\tag{1102.6}
$$
所以高度 Gram 是迹 Gram 复合 $w=\kappa a^{-1}$ 的乘法矩阵，
$$
\det(q^{-1}h)=\operatorname{disc}P\ \operatorname{Res}(P,w).
$$
逐因子 $\kappa$ 非零、$\gcd(\kappa,P)=1$、
以及该行列式非零三种判断均由成功消费者一致检查。
(1102.2)在整个整基上取整，双线性给整个 $M$ 的整性；
其模$q$行列式非零，再用 Nakayama 即得(1102.3)后的完美性。

## 5. 十六个原一次块的 log 归一系数

对 R1093 的原规范特征微分 $\omega_r$，设
$$
\lambda_r=q^{-1}\log(P_0)(\omega_r)\pmod q,\qquad
x_r(P)=q^{-1}\log(P)(\omega_r).
$$
每个 $\lambda_r$ 及特征向量规范哈希直接消费原已认证输入。
若 $r$ 是 $H$ 的一次根，则
$H_2=T_2+2T_3+4T_5$ 的标签由同一多项式桥取得，不能另猜匹配。
原 $q^{-1}h$ 在 $x_r$ 坐标中的系数是
$$
\mu_r=\frac{\kappa(r)}{a(r)\lambda_r^2}.
\tag{1102.7}
$$
本次实际结果如下，所有数在 $\mathbf F_{4513}$：

| 原 $H_2$ 标签 | $H$ 标签 | 原 $\lambda_r$ | $\mu_r$ |
|---:|---:|---:|---:|
| 434 | 2830 | 3527 | 176 |
| 1054 | 3651 | 1604 | 4441 |
| 1615 | 1945 | 1240 | 1081 |
| 2250 | 3950 | 725 | 661 |
| 2425 | 3657 | 420 | 3048 |
| 2472 | 179 | 3347 | 2669 |
| 2604 | 3783 | 1418 | 2442 |
| 2838 | 3379 | 3824 | 4286 |
| 3030 | 2590 | 3003 | 1125 |
| 3112 | 444 | 1974 | 2455 |
| 3531 | 630 | 3330 | 3820 |
| 3560 | 3131 | 4182 | 2924 |
| 3639 | 4279 | 3589 | 2655 |
| 3645 | 3857 | 3771 | 2746 |
| 3786 | 2779 | 3508 | 3505 |
| 3795 | 2542 | 3363 | 4377 |

若改用未除$q$的原 $\log(P)(\omega_r)$ 作变量，
$h$ 的系数为 $\mu_r/q$。保留移动单位 $a$、
原 $B$ 和实际微分规范；表中数不是未归一 log 的高度系数。

## 6. 输出与输入哈希

下表都是 SHA-256；脚本输出以 compact、排序 JSON 为哈希约定。
原日志中的 `completed` 对象保 Python 数字词法和键序后去除字符串外空格，
已逐字节核回完整结果哈希。不能把带整数键的原映射解析后
按字符串键重排，并误认为是同一序列化。

| 项 | SHA-256 |
|---|---|
| 脚本 | ca0c7d583d0c2feaadfb7bacd89552c52c888bcde145814db8934dc56eb87567 |
| 方法 | a073ee7c4d37396cb8e527f4a4c3175a75c7fb5af86d16e9cf5eb3649507ebb1 |
| 请求 | 3232e8a8aca7333aa45aa2daadc83edf1bcd8b66186dba73e80d44119e756cc7 |
| 完整成功结果 | d0977fa5bb669ee06f09b981951059029924a6693da2760fd54beaa391179e66 |
| 73个原指标高度 | 606bb972e02933a6697f0eb374041e405af82b5ce9d3036410fb8ad45f892047 |
| 73个 $H$ 矩 | c9d35ba97cfb2f46586bf3b6e726efe24069ec43d4cace38220a0dd873fc6996 |
| 迹 Gram | f9b5ac806b0bb42d47ab56dcc2be8c6d61f36de5fd154bc9eed687ef60b1874b |
| $\kappa$ 升幂系数 | 8bfe40fc3d7d7ffd5b5b80d6a9502f897d1e83e3c414de6dd51677be69d4b948 |
| resolvent 分子 | 91d92f69a41518bf0f650507e55106573045ea2cf1c7b70ce11ab6c29e3315db |

## 7. 后继范围

本结果支付原 full47 完整73维真实整格的首高度非退化性。
[R1103](R1103-original-CM-tangents-finite-field-third-kind-and-QC-first-jets.md)
的八个原 CM 圆盘还需实际切向、第三类微分读数、
对应的 CM 类坐标和最终共同零集判别。
本结果不单独推出任何一个圆盘的唯一性。

课题 README 要求全部充分大素数的 Serre 一致性；
固定47的完整第一层高度仍是中间结论，主目标继续。
