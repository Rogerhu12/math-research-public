# R150 Lt0：最小原 v 六次式的整个首项零面排空

日期：2026-11-27。AI-assisted GPT-6 Astra Pro；会话：Astra-ISP-8542378f-20261127。

**状态：已证明，完整原源已实际通过。** 在现余 S0/Lt0 原图中，最小 Cramer 子式 P045 对 v 的六次首项不能为零。此前已付原因子之外的整个 (4,4) 首项曲线 B44=0 已完整返回；只余的 e=1/2、两个 k 嵌入也在同一原二次域内由原 P045/P035 的 v-Bézout 单位排除。此后一般图可合法在 P045 给出的首项可逆六次商环中继续降低原方程次数。

本稿不声明一般图已空，亦不依赖四变量 Singular 门的状态。

## 1. 原六次式与完整首项

沿用[原低次不变量系统](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-low-invariant-original-system.md)及[原 Cramer 六行/二十子式](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-original-Cramer-minor-system.md)。记 e=u−1、k=Q/e、v=4kbc·t。行号按零起始为：0=N1elim，1/2=原 NB/PB 偶部，3=原 U 矩，4/5=两个原 mean 改写临界对。

使用此前完整关闭的 [k=4e](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-mean-consistency-line-exclusion.md)、[v=0](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-zero-singleton-pairing-exclusion.md)及 [Omega=2e²−ek+2=0](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-quadratic-invariant-curve-exclusion.md)整支。三者均独立于本稿。其余原单位以及 a=0、ell=1/2 已闭边界仍保持原来源。

令 P=P045 为已经剥除已付因子的原子式。它的 (e,k,v) 次数为 (19,16,6)，有 840 项。按自含源采用的归一化，完整 v 首项是

$$
\operatorname{lc}_v P=\frac1{524288}(4e-k)(ek-1)B_{44}(e,k),
$$

其中

$$
\begin{aligned}
B_{44}={}&-e^2k^4+(-16e^3-19e^2+e)k^3\\
&+(16e^4-40e^3-8e^2+36e)k^2\\
&+(16e^4-48e^3+64e^2+80e-16)k-64.
\end{aligned}
$$

源码实际乘回整个分解。4e−k、ek−1 已付，所以只须关闭 B44=0。同时

$$
\operatorname{lc}_k B_{44}=-e^2
$$

也是原单位；e=0 已由原 P02 非零关闭。这里没有隐藏未处理的 k 首项零分支。

## 2. 新的原 mean Dixon 必要式，有显式原组合

自含源从原 Gram、正确双点乘法和同根 P/N 重新生成所有输入，并保留全部 Cramer 组合乘回。下面只取三条原 mean 二次式 q1、q2、q3（E1、EB 偶部、EB 奇部），把 lambda、f 临时写成 x、y。

引入独立辅助变量 alpha、beta，定义真正的多项式差商

$$
X_i=\frac{q_i(\alpha,y)-q_i(x,y)}{\alpha-x},
\qquad
Y_i=\frac{q_i(\alpha,\beta)-q_i(\alpha,y)}{\beta-y}.
$$

两次分母都是单变量的差，不是参数逆。源码实际用精确整除并乘回。令

$$
\mathcal D=\det\begin{pmatrix}
q_1&q_2&q_3\\X_1&X_2&X_3\\Y_1&Y_2&Y_3
\end{pmatrix}.
$$

第一行展开立即给出三条原 mean 的明确多项式组合；源码逐项验证这一组合及

$$
(x-\alpha)(y-\beta)\mathcal D
=\det\begin{pmatrix}
q(x,y)\\q(\alpha,y)\\q(\alpha,\beta)
\end{pmatrix}.
$$

因此 alpha/beta 的每个系数本身属于原 mean 理想；没有使用多元结果式的泛性定理，也没有以零集采样替代原理想身份。

实际出现的辅助单项式是 1、beta、alpha、alpha beta、alpha²。取每个系数后，继续使用原三 mean 的已付 Cramer 矩阵把纯 lambda/f 二次项降到一次，并追踪、乘回每个原 mean 组合及分母。最后两系数返回零，前三系数给三条线性必要行，其项数依次为 768、597、549。

取这三行的完整 3×3 子式，并实际核对其原行组合，得到只含 (e,k,v) 的新必要式 D8，次数 (25,20,8)，1581 项。它是原 mean 的明确局部化组合。

源码中两个原本不出现在三 mean 中的变量槽仅作 alpha、beta 辅助变量，取系数后全部消去；这不是对物理 eta 或饱和变量赋值。

## 3. 保全 v 首项的三条二参数投影

把 P045 分别与 D8、P035、P034 作完整 Res_v。输入均是以上的原必要式；没有先令它们对 v 首一，也没有除 v 首项。即使 P 的首项在本分支恰为零，真实有限 v 公共根仍使每条完整结式为零。

每条结式仅剥已付单位（包括前三份独立排空支付的因子），所有剥除积实际乘回，得到三条二参数必要式 A、B、C：

| 投影配对 | 原结果式 (e,k) 次数 | 仅剥已付因子后的次数 |
|---|---:|---:|
| P045，D8 | (204,170) | (104,74) |
| P045，P035 | (180,155) | (132,109) |
| P045，P034 | (179,164) | (133,119) |

这一步没有选择某个未知不可约因子，也没有以这些多变量多项式的 gcd 推断空集。

## 4. B44 整曲线的完整一元覆盖

在 B44=0 上，原参数还须满足 A=B=C=0。分别计算完整

$$
\operatorname{Res}_k(B_{44},A),\quad
\operatorname{Res}_k(B_{44},B),\quad
\operatorname{Res}_k(B_{44},C).
$$

三个 QQ[e] 多项式的真实次数为 564、750、776。它们没有按任何 k 首项除法；原 B44 的 k 首项另外已由 e≠0 支付。

在 QQ[e] 逐次扩展 Euclid，保累计三输入组合并实际乘回，得到首一 gcd

$$
e^{69}(e-\tfrac12)^{106}(e+1)^{118}.
$$

e=0、e+1=0 已由原 u−1、u 单位支付。因此每个尚可能的 B44 原解必须有 e=1/2。这是完整一元覆盖，保留其全部重数，不遗漏任何投影降次参数。

## 5. 唯一剩余参数的同一原二次域返回

直接在原 B44 上代 e=1/2，源码核对完整分解

$$
B_{44}(\tfrac12,k)
=-\tfrac14(k-2)^2(k^2+29k+64).
$$

k=2 使 ek−1=0，违背原 p≠q 单位。其余两个 k 根保留在同一个原域

$$
K=\mathbb Q[k]/(k^2+29k+64).
$$

把原 P045、P035 直接返回 e=1/2 及此 K，在 K[v] 作扩展 Euclid。实际得到

$$
A(v)P_{045}+B(v)P_{035}=1.
$$

源码逐项核对两原输入的组合回乘；同时完成 8 次原域逆乘回、7 次 v 除法乘回。两个 k 嵌入始终共同保留，不分别取范数，也没有数值选根。

故唯一剩余二次域也无原解，B44=0 整曲线被排空。结合两个已付首项因子，原 P045 的整个 v 首项零面不存在物理解。

## 6. 一般图可用的准确后果

在现在的原图上，P045 的 v 六次首项是单位。因此可以把它除以该完整首项，在原已付局部化上形成首一六次关系，并用原多项式除法降低其他 v 式的次数。任何新余式都仍须保原组合；本稿没有把这一步降次当作整个一般图的排空。

## 7. 真实执行

[自含源](../notes/2026-11-27-unit211-S0-Lt0-original-v-leading-zero-return-8542.py) 28,962 字节，SHA256：

```
9e17050e11f5b66eb06860423b863cf7a9088a2aba80fc3b0ae4df19e3fe6407
```

[实际回执](../notes/2026-11-27-unit211-S0-Lt0-original-v-leading-zero-execution-8542.json)：Python 3.12.14、python-flint 0.9.0，180 秒 alarm、4 GiB 地址空间上限；真实 exit 0，109.809478 秒，峰值 RSS 607,860 KiB。全部原 Gram/Cramer、Dixon 差商原组合、两层完整投影、累计一元 Bézout 与末二次域返回均实际通过。

末三条一元投影 SHA256：

```
3d653ebba4802fd57eeb720c7c2e71bd410fc6abfbb3a461b6dba608210846f1
2f23bf0e15309e2f7b92c320f479447a44506f52f8c372c7f7b6bc14642487c9
19a8367b4bc9ebcff47f2ce2cac401e3433eec8ee0ec1b45b514b78840c1d969
```

累计一元 Bézout 系数 SHA256：

```
45a80d533d8fd1eef585d44aeeee905ff483ae57996ab68bf0ffa6ef59fc3e92
```

可重算大系数仅在内存生成，不入仓保存。本稿不使用也不重跑已废止的旧均值投影或原有失败门。
