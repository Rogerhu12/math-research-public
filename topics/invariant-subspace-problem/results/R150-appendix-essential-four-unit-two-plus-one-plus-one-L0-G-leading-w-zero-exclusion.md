# R150：L0 的 G 曲线全部 w 首项零纤维排除

日期：2026-11-27（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127；AI-assisted GPT-6 Astra Pro。

**结论。** 原 L0 剩余 G(lambda,w)=0 图中，G 对 w 的四次首项为零的整个分支为空。全部 lambda 零首项因子均覆盖，最后六维同参数原返回得到真实 Bézout 单位。因此后续可在全部剩余 G 图上合法用 G 的 w 四次关系，不丢弃首项零纤维。一般 G 曲线仍未排空。

## 1. 原输入与完整首项因子

沿用 [整个 P1 双零排除](R150-appendix-essential-four-unit-two-plus-one-plus-one-L0-P1-double-zero-complete-exclusion.md) 的同一 rho、lambda、w 坐标及原九式。G 为 [冻结原源](../notes/2026-11-26-unit211-L0-remaining-small-faces-original-QQ-lift-347c.py) 明列的 (lambda,w) 次数 (7,4) 多项式，不重新采样或替换曲线。

本次源从原 Gram 重建 P1、E1、EB、N1、PB、NB 的全部相关分量及必要结果式，保持原 kappa²=1−Q 的两根。准确首项为

$$
\operatorname{lc}_w G
=-8\lambda(\lambda-1)(4\lambda^2-5\lambda+2)(4\lambda^2-2\lambda+1).
\tag{1}
$$

原 lambda 非零已经支付；剩下三个完整因子分别处理。

## 2. 两个整参数域由原 w=0 或 w=1 支付

字面代入给

$$
G(1,w)=-4w(w-1).
$$

在整个 QQ[lambda]/(4lambda²−2lambda+1) 中，准确余式为

$$
G(\lambda,w)=-\tfrac14w(2\lambda-1)(w-1).
$$

2lambda−1 在该整个二次代数中的逆已由 QQ extended gcd 实际乘回。因此两类原解都迫 w=0 或 w=1，与已完整关闭的 L0 两条原分支矛盾。这些不是一般位置的代入；两个二次根均覆盖。

## 3. 剩余二次参数的完整六维原代数

现在 4lambda²−5lambda+2=0。原 G 的准确余式是

$$
32G=a(w)\lambda+b(w),
$$
$$
a=5w^3+89w^2+133w+13,\qquad
b=-18w^3-90w^2-82w-2.
$$

将 lambda=−b/a 代回只在证明 a 可逆之后进行。完整消元为

$$
4b^2+5ba+2a^2=32\Phi_6(w),
$$
$$
\Phi_6=28w^6+140w^5+270w^4+293w^3+221w^2+49w+7.
\tag{2}
$$

源直接验证 cover 与 a 的 QQ extended gcd 是常数，并将 a 的逆在 cover 商环中乘回为 1。因此 a=0 没有漏掉的原纤维；任何满足二次参数式和 G 的解都在完整代数

$$
\mathcal B=\mathbb Q[w]/(\Phi_6),\qquad \lambda=-b(w)a(w)^{-1}
$$

中。源另外逐项核对 4lambda²−5lambda+2=0 与 G=0；lambda 和 w 没有独立换嵌入。

## 4. 返回原 rho 与同一 t

令原 P1 为 alpha·t+beta。由已闭整个 P1 双零图，任何剩余原解上 alpha 不为零。对原必要式 E1、N1，使用原系数返回多项式

$$
F_E=\alpha^{\deg_t E_1}E_1(-\beta/\alpha),\qquad
F_N=\alpha^{\deg_t N_1}N_1(-\beta/\alpha),
$$

并只剥除已付物理单位。所有这些多项式已经由原 Gram 生成，保原 f 与全部相关参数。

在整个 B 中，把 F_E、F_N 返回为 rho 的一元多项式。原 F_E 中一个 rho 因子属于已付原 Q 单位，精确除去后 rho 次数为 4；它与原 F_N 的一元 gcd 立即为 1。计算包含 47 次基代数逆，所有逆、Euclid 除法和 Bézout 身份均实际回乘。

因此任一相关参数嵌入及同一 rho、t 的原解都会迫 Bézout 左边为零，与右边 1 矛盾。该原返回完整排除 (2) 的全部六维参数，不需要挑某个根或假设两个原 t 方程有不同的 t。

结合 §2 和原 lambda 非零，(1) 的全部零纤维排尽。

## 5. 执行身份与后续准确范围

[自含源](../notes/2026-11-27-unit211-L0-G-leading-w-zero-original-return-8542.py) 18016 字节，SHA256：

```
015ce3071c81b2bf532943207fb701a7ddb1b36d9607410e2ed3606bd7836296
```

[实际回执](../notes/2026-11-27-unit211-L0-G-leading-w-zero-execution-8542.json)：Python 3.12.14、python-flint 0.9.0，180 秒 alarm；实际 3.809899 秒，exit 0，峰值 RSS 52192 KiB。stdout SHA256：

```
d6d95fe60582c3ed3f99e54ed03fcb318980f51cca8897fdf9af8074414b14de
```

原 cover SHA256：

```
787160e6176bd1a5a14a8a0865f6b4b9811cc43358a604449abbb0beeaffdeb5
```

源没有重跑旧 G 的 4 GiB QQ 单位门，也没有重跑已完成的 P1 双零 lambda 投影。当前新增的是这一完整首项零支及原相关返回。剩余 G 上可以合法使用 w 四次商关系，仍须处理一般原解及其余 L0 交点。
