# R150 Lt0：原均值乘法一致性的 k=4e 整支为空

日期：2026-11-27。AI-assisted GPT-6 Astra Pro；会话：Astra-ISP-8542378f-20261127。

**状态：已证明，完整原源已实际通过。** 在现余 S0/Lt0 原图中不存在

$$
Q=4(u-1)^2.
$$

在低次不变量 e=u−1、k=Q/e 中，这正是 k=4e。本证明不先除 4e−k；直接把原必要式返回整条线，并以两条完整一元结式的实际 QQ Bézout 身份排空。由此，后续一般图可合法把 4e−k 作为单位。普通不变子空间问题及其余 R150 分支没有因此完成。

## 1. 原图、已付单位与同一参数

沿用[原低次不变量系统](R150-appendix-essential-four-unit-two-plus-one-plus-one-S0-Lt0-low-invariant-original-system.md)。令

$$
e=u-1,\quad k=Q/e,\quad j=k+2-2e,\quad x=k+4,
$$
$$
D_3=4e^3-3e^2k-4e^2+ek^2+4ek+4e-k-4,
\qquad v=4kbc\,t.
$$

原 Lt0 给出 ell=j/k、u=e+1、Q=ek、T0=−ex 和

$$
bc=\frac{D_3}{4k(ek-1)}.
$$

原未除法身份

$$
P_{02}-2\ell Q(u-1)=-u\{T_0+4(u-1)+Q\}
$$

配合 Lt0 与 P02≠0 支付 ell、Q、e；u=e+1 则由已闭的[整个零基点 mean 分支](R150-appendix-essential-four-unit-two-plus-one-plus-one-zero-base-mean-exclusion.md)支付。k、j、D3、x、ek−1 为原物理单位；e−1=0 对应已闭 a=0，4e−k−4=0 对应已闭 ell=1/2。这里未把 L0 的权和结论用于 S0。

以下所有分母和剥除因子仅使用这些已付单位；尚未支付的 4e−k 始终保留直到最后的整支排空。

## 2. 从原 Gram 到六条带组合证书的线性行

[自含精确源](../notes/2026-11-27-unit211-S0-Lt0-mean-consistency-degenerate-line-return-8542.py) 从原 Frobenius Gram 和双点乘法重建原 mean、最高式 P 与第二矩式 N。其双点平方分量实际为 (d·d)1=2d0d1；源不读取任何旧 scratch 投影。

前三个 mean 为 E1、EB 偶部、EB 奇部，第四原式为

$$
N_{01}-(4\lambda/3)P_{01}.
$$

令 C 是前三原式对 (lambda²,lambda f,f²) 的系数矩阵。源码实际检查九个伴随矩阵乘回身份及

$$
\det C=-512e(e+1)(4e-k-4)k^2(-j)^3D_3^3.
$$

因此全部 Cramer 分母已付。对任意此次使用的多项式 p，递归降纯 lambda/f 二次单项式时同时追踪三个原 mean，并逐项检查

$$
p-\operatorname{NF}(p)=q_1E_1+q_2E_{B,+}+q_3E_{B,-}.
$$

每个有理系数分母都实际按 det(C) 因子剥除至常数。

新增原 NB、PB 的偶部来自完整孤立 B/C 点的原条件。原同一根表示为

$$
r^2=1-Q,\qquad H=\lambda-\tfrac12,\qquad
h=H+\frac{\eta}{2(1-Q)}r,
\quad \eta=\theta\Delta.
$$

源码先核 h²、h³ 的同根降幂误差均为原范数式 eta²−(1−Q)Delta 的显式倍数，再生成

$$
N(K_B)-2\lambda P_{02}h^2,\qquad
P(K_B)-P_{02}h^3.
$$

原 C 点是同一 r 的共轭。没有独立取范数或混合两次选择的根，也没有除 h。原 P1 和 U 矩给出的 z=Znum/(2j²) 也逐项乘回，j 已由原 P02 支付。

得到以下六条对 lambda、f 一次的原必要行 Li=ai lambda+bi f+ci：

| 零起始行号 | 原来源 |
|---|---|
| 0 | N01−(4lambda/3)P01 |
| 1 | 原 NB 偶部 |
| 2 | 原 PB 偶部 |
| 3 | 原 U 矩 zT=C0 |
| 4 | 原 mean 改写临界对 fR(lambda²)−lambda R(lambda f) |
| 5 | 原 mean 改写临界对 fR(lambda f)−lambda R(f²) |

临界对本身的原 mean 组合也在归约之前实际核对。

对三行 A、B、C，取其 (ai,bi,ci) 的 3×3 行列式 D。因为线性行的第三坐标是 1，具有完整多项式身份

$$
D=(b_\lambda c_f-b_fc_\lambda)L_A
-(a_\lambda c_f-a_fc_\lambda)L_B
+(a_\lambda b_f-a_fb_\lambda)L_C.
$$

源码逐条检查全部二十个子式的这个原行乘回，每次只剥已付因子且反乘核对。本证明只需其中三个；保留其全部因子直到专门返回 k=4e，不使用一般位置的秩断言。

## 3. 整条 k=4e 的原返回

直接代 k=4e，源先核

$$
j=2(e+1),\qquad D_3=4(2e-1)(e+1)^2,
$$
$$
ek-1=(2e-1)(2e+1),\qquad 4e-k-4=-4.
$$

这些是已付原因子在该线上的精确身份。选 D034、D012、D013，代入后分别剥去仅来自已付 j 与 ek−1 的因子，并按一个非零有理常数归一化，得到 F034、F012、F013。每个式子均实际核对

$$
D_{ijk}(e,4e,v)=U_{ijk}(e)F_{ijk}(e,v),
$$

并把 Uijk 的全部因子按已付单位剥到非零常数。

| 原行子式 | 对 (e,v) 的次数 | 项数 | 归一化原多项式 SHA256 |
|---|---:|---:|---|
| F034 | (9,5) | 37 | `4c135be6b8c9f6c3d2bb344b2068e869b233f50834b4662d4a84190505f1acff` |
| F012 | (16,6) | 87 | `ffb9d81978b70b129ae6525ef594cd39d28d980ab751102c4dbc09682e901807` |
| F013 | (17,6) | 93 | `220ddd4a6c6f3b3c81aa92c0d194eea919c18f2ef56429e98b3c0d875113305f` |

原解必须同时满足这三个原返回式。取完整 Sylvester 结式

$$
R_{90}(e)=\operatorname{Res}_v(F_{034},F_{012}),
\qquad
R_{95}(e)=\operatorname{Res}_v(F_{034},F_{013}).
$$

实际次数为 90、95。因为没有按 v 首项除法，任何 v 首项为零、次数下降或返回式恒零的参数纤维仍必须使这两条完整结式都为零；没有遗漏例外纤维。

## 4. 特征零的一元 Bézout 矛盾

源码在 QQ[e] 实际运行扩展 Euclid，并核出

$$
\gcd(R_{90},R_{95})=e^{10}(e+1)^{40}.
$$

更强地，实际生成次数分别为 44、39 的 A(e)、B(e)，逐项乘回

$$
A(e)R_{90}(e)+B(e)R_{95}(e)
=e^{10}(e+1)^{40}.
$$

原解令左侧为零，而 e、e+1 都是已付原单位，右侧不为零，矛盾。这是**一元**完整结式的特征零 Bézout 证书；没有把多变量 gcd=1、有限域样本或数值残差当作排空。

因此 k=4e 的整条原支路为空，后续一般图可以支付 4e−k。

## 5. 实际执行

[运行回执](../notes/2026-11-27-unit211-S0-Lt0-mean-consistency-degenerate-line-execution-8542.json)记录 Python 3.12.14、python-flint 0.9.0 下真实 exit 0、3.421194 秒；完整原 Gram、同根 P/N、Cramer 追踪、子式和两条投影/一元 Bézout 全部实际通过。没有调用 Singular，也未登记整体 S0/Lt0 已空。

源 SHA256：

```
aa378c33ff3aaca8fc110097141ff51d88fc90bee5cebf6f03abd31ce64e905e
```

两结式 SHA256 分别为：

```
9803eb2e8e2612514e9c0a33f23a88a4b250cb40931046f81b931f393deb1be6
2740fcc27da62fd397df26a3935df45db7d546bc261fae0f6927743543ef6d16
```

实际 Bézout 三元组 (A,B,gcd) SHA256：

```
d2d2266eb1b82a37022e57b332df5a04eedf9f7abeb958ba25b67a7c77918bde
```

全部大系数从自含源重算，不入仓保存。
