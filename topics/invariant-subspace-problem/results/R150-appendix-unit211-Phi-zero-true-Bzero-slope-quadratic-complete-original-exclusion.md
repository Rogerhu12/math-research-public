# R150 补充：正确 Phi 整 B 曲线的斜率二次纤维完整排除

日期：2026-11-28（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。AI-assisted，GPT-6 Astra Pro。

## 1. 新完整结论

保持当前正确原 unit211 的
$$
\Phi=0,\qquad Q(1-Q)P_fP_{02}bcD\ne0.
$$
在正确三均值首项曲线
$$
B=-Q^2+(12u^2-20u+8)Q-16(u-1)^2=0
$$
上，沿[完整有理图](R150-appendix-unit211-Phi-zero-true-Bzero-rational-and-exact-six-by-two-model.md)令
$$
x=\frac{Q}{4(u-1)},\quad
u=\frac{(x+1)^2}{3x},\quad Q=\frac{4(x^2-x+1)}3.
$$
本条证明该图的新斜率因子
$$
\boxed{C(x)=23x^2-11x+2\ne0.}
\tag{1}
$$
这是整个二次纤维的特征零原排除，不是模筛选，也不依赖先前六乘二源最后 JSON 打印是否成功。整个 $B=0$ 尚未由本条排空。

记
$$
F=x^2-x+1,\quad H=2x-1,\quad
\beta=5x-1,\quad J=7x^2-4x+1.
$$
完整原参数单位给
$$
xF(x+1)H\beta J\ne0.
\tag{2}
$$
本次不倒三次头 $H_3$，也不倒斜率 $C$。

## 2. 整个二次域与同一原 Gram

反设 $C(x)=0$。其判别式是 $-63$，故在 QQ 上不可约。本次全过程在
$$
K=\mathbb Q[x]/(23x^2-11x+2)
\tag{3}
$$
内进行，保留两个复嵌入。每个需要的常数逆都用 QQ 一元 xgcd 返回完整 Bézout，再在 (3) 乘回。因而没有只对一个数值根进行计算。

在自由变量 $(\lambda,f,t)$ 上定义
$$
\ell=\frac{(x+1)\beta}{6x^2},\quad
\delta=1-Q=-H^2/3,\quad
bc=\frac{(x+1)^2J}{36x^4},
$$
$$
K_0=\frac{4F(x+1)}{3x},\quad
T_0=-K_0,\quad
P_{02}=\frac{4F^2(x+1)\beta}{27x^3},
$$
$$
T=\frac{3(x+1-f)}{\beta}-\frac{x+1}{x}\lambda-\ell,
$$
$$
A_1=\frac{2F(f-x-1)}{3x^2}
+\frac{2F(x+1)\beta}{9x^3}\lambda.
\tag{4}
$$
这些是原 $E_0/N_0/P_1$ 的同点恢复，全部在 (2) 内合法。

令
$$
V=f-A_1/2+bc\,t,\quad W=-K_0/2+2uf,\quad
m=u-\ell,\quad M=4bc\delta.
$$
真实 singleton 坐标由
$$
x_0=\frac{(u-\ell Q)V-mW}{M},\qquad
y_0=\frac{\ell W-uV}{M},\qquad
X=x_0+\rho y_0,\quad Y=x_0-\rho y_0
\tag{5}
$$
恢复，其中形式二次代数 $\rho^2=\delta$ 保留两根。权重是
$$
b=\frac{\ell}{2}-\frac{(x+1)(x-1)}{4x^2H}\rho,\qquad
c=\frac{\ell}{2}+\frac{(x+1)(x-1)}{4x^2H}\rho.
$$
令 $a_w=1-\ell$、$p=1+\rho$、$q=1-\rho$、
$r=X-a_wp-ct$、$s_G=Y-a_wq-bt$。使用原四行
$$
(0,0,p,q),\quad(0,A_1,r,s_G),\quad
(p,r,0,t),\quad(q,s_G,t,0).
\tag{6}
$$
本次实际返回 $F_2=2f$、$E_0=0$、$N_4(g_0)=2\lambda P_{02}$、原 $P$ jet 与全部权关系。原乘法始终是正确 dual 乘法，未使用撤回的 $R_{\rm bad}$。

## 3. 不倒三次头的原均值线性关系

写原 singleton 均值
$$
E_B=E_{\rm e}+\rho E_{\rm o}.
$$
以真实 germ 均值 $E_1$ 构造纯权乘子
$$
\begin{aligned}
\kappa_0&=-18x^3H,\\
\kappa_1&=2-13x+54x^2-79x^3+68x^4,\\
\kappa_2&=H(-2+15x-54x^2+97x^3-48x^4).
\end{aligned}
$$
定义同一原组合
$$
\mathcal L=\kappa_0E_1+\kappa_1E_{\rm e}+\kappa_2E_{\rm o}.
\tag{7}
$$
它的 $f,t$ 二次项精确抵消。在 (3) 上，令 $a=[\lambda f]\mathcal L$；本次完整返回 $a$ 为 $K$ 的单位，且
$$
\frac{\mathcal L}{a}
=(\lambda+\tfrac14)
\left(f-\frac{5-23x}{16}t\right)+p_0(\lambda),
\tag{8}
$$
其中
$$
p_0(\lambda)=
\frac{19x+4}{12}\lambda^2+
\frac{103x-47}{24}\lambda+
\frac{5(x-1)}{16}.
\tag{9}
$$
源码按 (6)、(7) 直接提取全部系数并返回 (8) 的原线性恢复；没有从零集猜测替代方程。

在 $\lambda=-1/4$，
$$
p_0(-1/4)=\frac{38-127x}{192}\ne0\quad\hbox{于 }K.
\tag{10}
$$
其完整逆可写为 $(-1046+5842x)/129$，模 (3) 乘回为 $1$。所以 (7) 排空 $\lambda=-1/4$ 的整个原纤维，合法支付
$$
4\lambda+1\ne0.
$$
现在 (8) 唯一恢复
$$
f=\frac{5-23x}{16}t-\frac{4p_0(\lambda)}{4\lambda+1}.
\tag{11}
$$
所有 $t$ 仍保留，没有倒 $t$ 或一个未知 $t$ 首项。

## 4. 完整原值的一元 t 投影

将 (11) 代入同一 (6) 的
$$
E_1,\quad E_{\rm e},\quad E_{\rm o},\quad N_1,\quad NS,\quad PS.
$$
这里 $N_1$ 是原极化值减 $4\lambda wP_{02}$；$NS,PS$ 是完整 weighted N/P 条件。按各原式的 $f$ 次数乘以 $(4\lambda+1)^d$，逐项返回整个多项式，得到 $K[\lambda,t]$ 内的六个真实必要式。

实际次数为：

| 原式 | $t$ 次数 | $\lambda$ 次数 | 清除的 $4\lambda+1$ 幂 |
|---|---:|---:|---:|
| $E_1$ | 2 | 4 | 2 |
| $E_{\rm e}$ | 2 | 4 | 2 |
| $E_{\rm o}$ | 2 | 4 | 2 |
| $N_1$ | 1 | 4 | 2 |
| $NS$ | 3 | 6 | 3 |
| $PS$ | 3 | 6 | 3 |

特别是原 $N_1$ 的 $t^2$ 系数在完整 (3) 内精确为零，实际成为一次式；这不是某个素数下的降次观察。

以这条 $N_1$ 为固定原锚，分别作关于 $t$ 的五个 Sylvester 行列式。对前三条均值，固定次数为 $(1,2)$、阶数 $3$，真实 $\lambda$ 次数均 $10$；对 $NS,PS$，固定次数为 $(1,3)$、阶数 $4$，真实 $\lambda$ 次数均 $15$。

任一原点的同一个有限 $t$ 根迫使五个固定行列式都为零。任何特殊 $\lambda$ 上的 $t$ 首项下降仍被该固定矩阵保留，无须先排除这些首项零纤维。

完整 $K[\lambda]$ Euclid 和 Bézout 返回
$$
\boxed{\gcd(R_{E_1},R_{E_{\rm e}},R_{E_{\rm o}},R_{NS},R_{PS})
=(\lambda+\tfrac14)^2.}
\tag{12}
$$
累计次数为 $10\to2\to2\to2\to2$。每次除法及每次完整 Bézout 组合均乘回；在第二个投影后已经得到同一平方，后两条完整值没有引入额外共同根。

(10) 已经排除 (12) 的唯一根。因此整个 (3) 的原纤维为空，得到 (1)。这里未从模空性推出特征零，也没有把 $D=0$ 的模迹当成原判别式零。

## 5. 唯一实际源与边界

[自含新源](../notes/2026-11-28-unit211-Phi-zero-true-Bzero-Ctwo-original-fixed-t-return-8542.js)：

- blob 66c2730080419c1a6ad2d04150872f75b17b804b；
- SHA256 45dba5c56f6efdf075451489b043cec89d102edcf0ebd629768457cd2a7ce3fc；
- 18474 字节，纯 V8 BigInt；
- 首次实际 23103 ms；
- 6552 次整数多项式乘法，738 次整数整除乘回；
- 7318 次整个 $K$ 的乘法、45 次实际逆；
- 153 次 $K[\lambda]$ 多项式乘法，19 次完整除法及 Bézout 返回；
- 五个固定 Sylvester、(10)、(11)、(12) 全部完成。

[小回执](../notes/2026-11-28-unit211-Phi-zero-true-Bzero-Ctwo-original-fixed-t-return-execution-8542.json)保留真实执行身份。本次没有重跑 B 的六乘二门、旧 GB 或其他资源冻结门。

现在正确整 $B$ 上的二次斜率纤维已排除。三次头 $H_3=0$ 是此前选取三条原式的局部化边界；它不能仅因本条 (1) 而被称为排空。下一步可由已成完整四头单位理想胶合，或用别的真实原输入处理；整个 Phi 和普通 ISP 仍未完成。
