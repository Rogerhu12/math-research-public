# 正确 Phi：B=0 的两个完整大常数域中，原线性行与首一二次的固定结式

- 日期：2026-11-28（Asia/Taipei）
- 本文是首次新输入说明，不是已运行结论。
- 源：2026-11-28-unit211-Phi-zero-true-Bzero-large-fixed-original-norms-8542.py
- 源 SHA256：c6e8acc0e71c119fd76f8213f2934daacc8ec728cb44b5a51f8541413e3a6eef。
- 分别设置 ISP_B_FACTOR_DEGREE=34、40；两个独立首次工作流，每次 120 秒、1 GiB，外驱动 135 秒。

## 1. 与已冻结门的区别

两个 d825 首次运行已分别触及 1 GiB 内存边界，run 为 46124520657、46124522483。它们实际完成了原四式的首一 lambda 六次及完整 408、480 维环境，但没有返回大原理想矩阵的秩或正目标。

本输入不重启该完整有理矩阵，不提高预算，不换消元顺序重复它，也不再计算原 NS/PS 或正幂目标。本次新增的是四个原线性行分别与首一 omega 二次式的固定结式；它们没有在 d825 中计算过。d825 的旧标量只来自线性行彼此的两个系数行列式。

## 2. 完整常数域与既成六次输入

取已刊 C76 的两个真实不可约因子，令

$$
K_d=\mathbb Q[x]/(F_d),\qquad d\in\{34,40\}.
$$

两个精确因子 SHA256 分别为 b593d2770a0337dcaf2f4908e51cfc9feb3c5890ce21e5c3c6c1707ff98187ff 与 ba88a205beb579a18de711c9fd61514716099afeed94954736246cedf733a16a。参数定义、坐标分母和原行均取既存不可变源的必要前缀，不另存系数载荷。

在完整 $K_d$ 中已有

$$
q_\omega=\omega^2+q_1(\lambda)\omega+q_0(\lambda),\qquad
r_i=a_i(\lambda)+b_i(\lambda)\omega,\quad 0\le i<4,
$$

以及原关系 $g_d(\lambda)$，其中 $g_d$ 首一且次数 6。本源只由第一个非零原对

$$
c_{03}=a_0b_3-a_3b_0,\qquad
g_d=c_{03}/\operatorname{lc}_\lambda(c_{03})
$$

再生该已成输入，并核其精确系数串 SHA。两域对应 SHA 分别为 f2d41bd0b2b1623745f9e0fd69a0cb488650f07bcd264a3f18b4a63bf8188b0c 和 9a94efc0ec88870b215b47b5175bbc4832b9c3f75c66d14e16d59ab845198cfe。

不重跑旧六对 gcd 或旧首一六次的全部原组合证明。该输入恒等式的使用范围仍是完整常数域，保全部复嵌入。

## 3. 真正新增的固定原结式

对每个 $r_i=a_i+b_i\omega$ 定义

$$
n_i=a_i^2-q_1a_ib_i+q_0b_i^2.
$$

其完整恒等式是

$$
n_i=(a_i-q_1b_i-b_i\omega)r_i+b_i^2q_\omega. \tag{1}
$$

程序实际返回 $(1)$ 的全部三个 omega 坐标。因此 $n_i$ 是原理想中的标量，不要求 $b_i$ 是单位，不删去 $b_i=0$，也不需要根简单。它等于固定二次与一次 Sylvester 行列式，所以原一次首项退化仍由同一个多项式身份覆盖。

只对实际 $n_i$ 作首一 $g_d$ 短除，再对

$$
(g_d,n_0,n_1,n_2,n_3)\subset K_d[\lambda]
$$

进行新的完整扩展 Euclid。若 $n_i=q_i g_d+s_i$，则每次使用 $s_i$ 的组合都完整输送回 $n_i$ 和 $g_d$，不把短除余式的来源省略。

最终得到首一 $h_d$ 及真正恒等式

$$
h_d=\beta_g g_d+\sum_i\beta_i n_i.
$$

再将原 $g_d$ 的固定两行来源和 $(1)$ 复合，完整返回

$$
h_d=\sum_{i=0}^3(A_i(\lambda)+B_i(\lambda)\omega)r_i
       +C(\lambda)q_\omega. \tag{2}
$$

代码实际检查 $(2)$ 的全部三个 omega 坐标。已有整 B 两列呈示保证 $q_\omega$ 与各 $r_i$ 有真实原四式来源，因此 $(2)$ 可复合为同一原理想身份；不假定两生成元模块自由或裸矩阵结合。

## 4. 结论仅按实际返回

若实际 $h_d=1$，则这个完整 $F_d$ 权纤维由原四式排空。没有使用 D、lambda、t 或任何范数的逆。

若 $h_d$ 的次数仍为正，只登记新的首一必要关系及环境

$$
K_d[\lambda,\omega]/(h_d,q_\omega),
\qquad \dim_{\mathbb Q}=2d\deg h_d,
$$

不声称实际原理想余商达到该维数，不声称排空。所有剩余 lambda、omega 重数保留。

若运行未完成最终完整身份，保最后已返阶段和整个未闭纤维。另一个常数因子必须由其独立首次返回处理。两个独立结果全部成立之前，不宣称整 B 排空；任何时候都不据此宣称整 Phi 或普通 ISP 已解决。

## 5. 必要前缀与依赖

需在 runner 临时目录按同 basename 放置四个已存源码：

1. 2026-11-28-unit211-Phi-zero-true-Bzero-large-constant-original-fiber-8542.py，SHA256 a44a8fc4ca4842d97c4d94215250e8399f5988407c3971bdc68ffe96b3b77a48；
2. 2026-11-28-unit211-Phi-zero-true-Bzero-whole-I6-twelve-by-two-8542.py，SHA256 b802d6c9b7a46b544f1fd5f814b05337a552f938a660b8d047fe4e62ff4eae56；
3. 2026-11-28-unit211-Phi-zero-true-Bzero-terminal-original-multiplier-cancellation-8542.py，SHA256 73d4dd4167d48b5a5878338bdfe85dc6c59a194b97fa2ae23309e2c2226eac35；
4. 2026-11-28-unit211-Phi-zero-corrected-dual-germ-four-original-quadratic-heads-8542.py，SHA256 5ee86ff89db7c8babaf3a22c7d72570dcdfbbf92646f56adf37bff854a87ace7。

第一源只执行到 for i,value in enumerate(env['original']): 之前，共 9481 字符；这在旧原四式回查、六对 gcd、NS/PS 有限归约及完整理想矩阵之前。其嵌套来源只为准确常数参数、原行和运算定义。所有 alarm 请求受新源最初 absolute deadline 钳制，不会因前缀重置延长本次限额。源码不写系数文件，不输出大载荷。
