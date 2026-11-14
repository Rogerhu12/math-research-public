# 冻结 R52 profile 的一维第四纯通道诊断设计

日期：2026-11-14。这是首个完整第四试验之后的独立误差定位。实际 profile 积分仅在本公开仓库 Actions 运行；开发时只运行两个小型形式微分恒等式与人为 SHA 身份检查，没有计算真实 profile 的积分。

## 1. 固定身份，单独改变 profile quadrature

输入直接读取已经成功运行的

`notes/actions-43618467921-1-full_fourth_evaluate/full-fourth-function-evaluation.json`

并要求其原始 SHA256 为

`a9162b82535af2efacf1ad0e7f07ff0e6aa97991417d7c5de5cbd922f2ddb15a`。

其中 profile 身份是 `20680dfd98d6ede4db5ee5f0ec34dd24f0b10ceabdbad6d07364508cb7dae506`。程序重新核 canonical JSON 身份，不重新调用谱拟合，不调整任何多项式系数、幅度、位置、宽度或立方权。它另外核原 profile 生产器和 Gauss/右锚实现的源 SHA，防止冻结定义与实际调用的代码分离。

新的 `literature_frozen_profile_fourth_gate.py` 只使用原 `ProfileTable` 的 17 个 panel、五阶以下解析 input jets 和共同右端原函数；传入空的 profile atom 表，因此不会编译完整目标或构造 6365 个 Volterra atoms，也不进行几何积分。

两档为每 panel 256、512 点。这样可单独检查首轮 64、96 点 profile 积分是否充分，不再同时改变几何 quadrature。第一标准常态是 $k=0,h=1,\omega=0$，使用已冻结的正物理区间 $[l,r]$。结果仍只属于 R52 数值实例，不冒称是 R53 已支付最高项的 profile。

## 2. 两个直接式和一个局部式

记 $x=\xi,Q=1+x^2$，保留真实复尾

$$J(x)=\int_x^r\{Qq''^2+2q'^2\},\qquad J_{\rm tot}=J(l),$$

$$V=\mathcal R_0(q,q)=-\frac{Qq'^2+xJ}{8},\quad
a=xq''-q',\quad F=Qq''-2q,$$

$$V'=\frac{xQq''^2-2Qq'q''-J}{8},\qquad
V''=\frac14a(a+Qq''').$$

所有乘法均为普通复双线性乘法。定义

$$B_q=\frac12F^2-2Qa^2-Q^2a q''',\qquad
T(q)=\frac1{32}\int_l^r B_qV''.$$

由于 $q$ 紧支撑，R49 的分部积分在这里没有端项，即使 $V$ 因 $J_{\rm tot}\ne0$ 有左尾也一样。

程序分别评价实际物理能量

$$E_{\rm phys}(V,V)=\int_l^r\frac1{x^2}
\left\{\frac14(xV''-V')^2+
\left(V-xV'+\frac{x^2V''}{2}\right)^2\right\}\,dx,$$

以及常用的导数形式

$$E_{\rm Sob}(V,V)=\frac14\int_l^r QV''^2+\frac12\int_l^r V'^2.$$

两个对应第四量分别是

$$\mathcal F_{\rm phys}=E_{\rm phys}+2T(q),\qquad
\mathcal F_{\rm Sob}=E_{\rm Sob}+2T(q).$$

第三个评价是 R50 局部多项式按普通复平方延拓的

$$\mathcal F_{\rm loc}=\frac1{128}\int_l^r\mathcal Q(q,q',q''),$$

$$\begin{aligned}
\mathcal Q={}&2Qq''^2
\left\{\left(q-xq'+\frac{x^2-1}{6}q''\right)^2
+\left(q'-\frac x3q''\right)^2\right\}\\
&+\frac{Q^3}{36}q''^4
+4q'^2\left(q-\frac x3q'\right)^2
+\frac{2(x^2+3)}9q'^4.
\end{aligned}$$

这不是一个对复 profile 非负的表达式。

## 3. 未配平时不能忽略的两个准确端项

若 $J_{\rm tot}\ne0$，$V$ 在左 collar 为 $-xJ_{\rm tot}/8$，所以不能在有限区间直接把 $E_{\rm phys}$ 当成 $E_{\rm Sob}$。准确密度差为

$$\frac{d}{dx}\left\{VV'-\frac{V^2}{x}
-\left(\frac x2+\frac1{4x}\right)V'^2\right\}.$$

右端 $V=V'=0$，左端 $V=-lJ_{\rm tot}/8,V'=-J_{\rm tot}/8$，故

$$E_{\rm phys}-E_{\rm Sob}
=J_{\rm tot}^2\left(\frac l{128}+\frac1{256l}\right).\tag{1}$$

另一方面，置 $K=q'^2$、$A=Q(2q'q''-xq''^2)$，则

$$A=(QK)'+xJ',$$

$$J^2+2JA=(xJ^2+2JQK)'
+2Q^2q'^2q''^2+4Qq'^4.$$

左端 $K=0$，右端 $J=K=0$，积分给端项 $-lJ_{\rm tot}^2$。配合 R50 已核的局部多项式恒等式得到

$$\mathcal F_{\rm Sob}-\mathcal F_{\rm loc}
=-\frac l{128}J_{\rm tot}^2.\tag{2}$$

因此实际物理直接式的完整差是

$$\boxed{\mathcal F_{\rm phys}-\mathcal F_{\rm loc}
=\frac{J_{\rm tot}^2}{256l}.}\tag{3}$$

程序原样评价三个量及 (1)–(3) 的左右差，既不把 $J_{\rm tot}$ 强制设零，也不删除左 collar 的积分。只有准确尾条件支付后，三个量才都可视为 R54 的同一个纯最高次门。

## 4. 输出、计算范围和解释

每档保存三复总矩、实际 $J_{\rm tot}$、其正模比较尺度、$E_{\rm phys}$、$E_{\rm Sob}$、$T$、三个第四量、两个准确端项和三个身份残差。普通复数都以 `[real,imaginary]` 保存，不丢虚部，也不以绝对值代替需要的复函数。

直接积分项的绝对和只用来展示相消规模，不是接受容限。Gauss 节点从 binary64 构造再用 long double 传播，所有结果都不是区间包络。

本诊断可以回答：被冻结 R52 profile 的三矩误差是否稳定、局部纯最高项是否稳定、尾和能量端项是否与直接实现一致。它不评价 $K_2$、其他常状态、连接段、整个第四周期函数或全局 ruling gauge。因此无论结果如何，都不能单独判定完整第四 range 已支付。

输入几何只保留身份引用，不运行几何 ODE。任何后续改变 profile 系数或几何都必须是另一个设计身份。

## 5. 唯一实际 CLI

```sh
python topics/visible-flex-new-mechanism/scripts/literature_frozen_profile_fourth_gate.py \
  --input topics/visible-flex-new-mechanism/notes/actions-43618467921-1-full_fourth_evaluate/full-fourth-function-evaluation.json \
  --input-sha256 a9162b82535af2efacf1ad0e7f07ff0e6aa97991417d7c5de5cbd922f2ddb15a \
  --nodes 256 512 --max-seconds 120 \
  --out topics/visible-flex-new-mechanism/notes/frozen-R52-profile-fourth-gate.json
```

实际分支检查 `GITHUB_ACTIONS=true` 且 `GITHUB_REPOSITORY=Rogerhu12/math-research-public`。输出为小型 JSON，不保存节点大数组。

本地只运行 `--toy-only`：核 (1) 的密度总导数、(2) 的尾恒等式以及一个人为 JSON 的 canonical SHA 验证；没有评价任何真实 profile。配套 toy 输出为 `notes/literature-frozen-profile-fourth-gate-toy-20261114.json`。
