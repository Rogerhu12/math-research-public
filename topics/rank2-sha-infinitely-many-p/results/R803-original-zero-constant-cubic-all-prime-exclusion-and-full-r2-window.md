# R803 — 原零常数 charge 的全部三次 r=2 强窗口对所有素数排除

日期：2026-11-15。**状态：下述全素数排除已证明，包含原 $\ell=1,2$。**

R797 支付了 $q(t,0)=0$ 的移动常数因子和六十四个真实来源格。
本篇以完整有理最大子式及全部剩余特征的原非齐次矩阵关闭
$r=2,\ b=b_0=3$ 的这一分支。
大素数门先覆盖全部 $p>407$；实际十九角把剩余问题压成四个素数上的
二十一类来源。公共精确执行中，它们的全部四十个出现均不相容。

这里是原因子不存在的结论，不是一个新的 Sha 非零结论。
它不将标量投影后的 cube 替换原 $P^{\rm fact}$，也不变更同一个首次修正 R。

## 1. 定理与不依赖 ell 的真实长度

保持原 $\mathbf F_p$ 上的
$$
P^{\rm fact}=qt^2F^3\in\overline{\mathcal W}_D,\qquad
q=d^{-C_D}Q,\quad Q\in\mathbf F_p[t,Y],\quad d=1+8t,\quad f_D<p,
$$
$$
F\text{ primitive 不可约},\quad
b=b_0=\deg_YF=\deg_YF(0,Y)=3,\quad
F(0,1)=0,\quad F_Y(0,1)q(0,1)\ne0,
\tag{1}
$$
$$
0\le k_{\rm carry}=2h+2-s<\ell\le2,\qquad
3>4k_{\rm carry}+2,\qquad p=6s-1>101.
\tag{2}
$$
令 C 为原十九角曲面中的严格变换，$\kappa=C^2$。
保真正接触及原 M 的强窗
$$
\operatorname{ord}_tF(t,g(t))=h,\qquad
T_M=s-2-13,\qquad T_M-h>\kappa.
\tag{3}
$$

**定理。** (1)—(3) 与 $q(t,0)=0$ 不能同时成立。

由 (2) 立刻有 $k_{\rm carry}=0$，所以
$$
\boxed{s=2h+2,\qquad p=12h+11,\qquad
T_M-h=h-13,\qquad h\ge\kappa+14.}
\tag{4}
$$
这些式子与 $\ell$ 是1还是2无关。
下面只使用原来源、接触 $<s$、全部角帽及 (4)，
不使用一个只在 $\ell=1$ 才成立的第三块或 Bockstein 公式。
因此同一次因子存在性判定合法覆盖 $\ell=2$。
原两条十三行没有被删除；(3)、(4) 中的 $-13$ 正是其真实长度代价。

## 2. 同一个 F 的六十四格和准确右端

R792、R797 给出
$$
q=Y\widetilde q,\qquad
\widetilde q(0,Y)=c_q\in k^\times,\qquad -v_0(\widetilde q)=0,
$$
$$
F_0=\lambda d^cH,\quad H\text{ monic},\quad(H,d)=1,\quad
z=\deg H\in\{0,1,2\},\qquad G=\frac{F}{\lambda d^c},\quad G_0=H.
$$
这里 $H(0)$ 可以为零。
同一个 F 满足某个原 mask 的返回
$$
t^2YA_*G^3\in\overline{\mathcal W}_{3b+1},\qquad
A_*=(t-1)^id^jh_7^k,\quad i+j+2k\le6-3z,
\tag{5}
$$
其中 $h_7=16t^2+4t+7$ 在 $k=\mathbf F_p$ 上不可约。
$z=0,1,2$ 分别有50、13、1个 mask；
合并完全相同的角上界后共有56个格。

每格的最大亏损为
$$
M_h=\min\!\left(3,\left\lfloor\frac{4k+1}{3}\right\rfloor\right),
\quad M_1=\min(3,i),\quad
D_d=\left\lfloor\frac{2j+1}{3}\right\rfloor,\quad
D_\infty=\left\lfloor\frac{13-2(i+j+2k)}3\right\rfloor.
$$
对 $1\le n\le3$，其全部正 charge 系数是
$$
r_n p_n,\quad
r_n=h_7^{\,\max(0,\lceil(n-M_h)/4\rceil)}
 (t-1)^{\,\max(0,\lceil(n-M_1)/3\rceil)}
 d^{-\lfloor(n+D_d)/2\rfloor},
$$
$$
\deg p_n\le
\left\lfloor\frac{9n+D_\infty}{2}\right\rfloor-\deg r_n.
\tag{6}
$$
$n\le3$ 时原零角 $t^{\lfloor n/4\rfloor}$ 恰为1。
这保所有原多项式乘子，且有理次数包含 d 分母。

沿同一个原低轴
$$
\rho=d\Theta^{17},\qquad g\equiv\rho\pmod{t^s},\qquad
\log\Theta=-\sum_{n\ge1}\frac{q_n^\Theta}{3n}t^n,
$$
$$
q_1^\Theta=-\frac25,\qquad
q_n^\Theta=q_{n-1}^\Theta\frac{6n-4}{6n-1},
\tag{7}
$$
实际接触为
$$
G(t,\rho)\equiv0\pmod{t^h}.
$$
将 $H=t^z+\sum_{j<z}h_jt^j$ 的低系数保为未知列，
真实右端是 $-t^z$，不是随意改成常数 $-1$。
所有读取都在 $h<s$；这里没有以 $\rho$ 替换未付的原高尾。

## 3. 两个真正最大子式覆盖全部大素数

固定一格，令 N 为 (6) 的正 charge 列总数。
再添常数列 $1,t,\ldots,t^z$，完整列数为 $N+z+1$。
这些常数列在行 $0,\ldots,z$ 构成单位块。

producer 对完整列分别取以下两组行：
$$
\{0,\ldots,z\}\cup\{z+1,\ldots,z+N\},
$$
$$
\{0,\ldots,z\}\cup\{z+2,\ldots,z+N+1\}.
\tag{8}
$$
其行列式在消去常数单位块后，准确就是正 charge 的两个连续
$N$ 阶子式。程序逐行清分母，再在整数中用 Bareiss 消元计算，
每次整除都核余数为零。

公开完整执行的结果为：

- 全部56格的两子式均非零；
- 每格两子式的整数 gcd 均已完整试除，剩余因子恰为1；
- 所有这些 gcd 的素因子均不超过283；
- 全部所用行的最大指标为33。

这是真正有理子式及其全部共同坏素数，不是若干特征的抽样。
式 (7) 在行 $n\le33$ 的分母只可能含不超过 $6n-1\le197$ 的素数；
固定角乘子与 d 的整数幂级数不增加大素数分母。
故 $p>407$ 时，每格至少一个 (8) 子式在目标 p 处为单位。
由 (4)，这时 $h\ge34$，全部所用行都在真实接触前缀内。
所以非零 G 不可能满足接触：
$$
\boxed{p>407\quad\Longrightarrow\quad\text{无 (1)—(3) 的候选}.}
\tag{9}
$$

最高行33来自 $z=0,A_*=h_7^2d$ 的32个正 charge 列，
即 R802 的唯一同 charge 返回例外。
本篇直接保该整个32列格，不借 R802 的较小返回替换它。

## 4. 小自交数的完整二十一类

R797 给出原十九角的准确关系
$$
\begin{aligned}
|\boldsymbol\mu_h|&=3-m_h,&
|\boldsymbol\mu_1|&=3-m_1,\\
|\boldsymbol\mu_d|&=2c-\delta_d,&
|\boldsymbol\mu_\infty|&=2v-\delta_\infty,\quad v=u-c,
\end{aligned}
$$
其中序列长度分别为4、3、2、2，均非负非增；两 h7 链相同。
原零角四步链全为零。
另保
$$
\mu_{d,1}\le c,\qquad
\mu_{\infty,1}\le v-z,\qquad
\delta_\infty\ge2z,
$$
$$
\kappa=36+6(c+v)-2\sum\mu_h^2-\sum\mu_1^2
-\sum\mu_d^2-\sum\mu_\infty^2,
\quad
\chi=9+2m_h+m_1+\delta_d+\delta_\infty.
\tag{10}
$$
特别 $\kappa\ge9+6z$。

写
$$
E_h=2(9-\sum\mu_h^2),\quad E_1=9-\sum\mu_1^2,\quad
E_d=6c-\sum\mu_d^2,\quad E_\infty=6v-\sum\mu_\infty^2.
$$
于是 $\kappa=9+E_h+E_1+E_d+E_\infty$，每项非负。

在 $\kappa\le17$ 时，$E_h$ 只有0或8，
分别对应 $(3,0,0,0)$ 和 $(2,1,0,0)$。
$m_h\ge1$ 时最小 $E_h$ 已为10。

$z=0$ 时，d 和 $\infty$ 的全部贡献不超过8者由下表给出。
对 d 取 $(w,\delta,\boldsymbol\mu)=(c,\delta_d,\boldsymbol\mu_d)$，
对 $\infty$ 取 $(v,\delta_\infty,\boldsymbol\mu_\infty)$。

| 贡献 E | w | $\delta$ | $\boldsymbol\mu$ |
|---:|---:|---:|---|
| 0 | 0 | 0 | $(0,0)$ |
| 4 | 1 | 0 | $(1,1)$ |
| 5 | 1 | 1 | $(1,0)$ |
| 6 | 1 | 2 | $(0,0)$ |
| 7 | 2 | 1 | $(2,1)$ |
| 8 | 2 | 2 | $(2,0)$ |

$w\ge3$ 的最小贡献为9；$w=2$ 的其他允许序列贡献至少10。
$E_1\le8$ 的全表为：

| $E_1$ | $m_1$ | $\boldsymbol\mu_1$ |
|---:|---:|---|
| 0 | 0 | $(3,0,0)$ |
| 4 | 0 | $(2,1,0)$ |
| 5 | 1 | $(2,0,0)$ |
| 6 | 0 | $(1,1,1)$ |
| 7 | 1 | $(1,1,0)$ |
| 8 | 2 | $(1,0,0)$ |

因此 $z=0$ 的全部类是：

1. $E_h=E_d=E_\infty=0$，$E_1$ 取表中六值；
2. $E_h=E_\infty=0$，
$(E_d,E_1)=(4,0),(4,4),(5,0),(6,0),(7,0),(8,0)$；
3. 与上一项交换 d、$\infty$ 的六类；
4. $(E_h,E_1,E_d,E_\infty)=(0,0,4,4)$；
5. $(E_h,E_1,E_d,E_\infty)=(8,0,0,0)$。

合计二十类，全部保表中完整重数序列。

$z=1$ 时，$\mu_{\infty,1}\le v-1$ 迫：
若 $v=1$，只有 $\delta_\infty=2$、$\mu_\infty=0$、$E_\infty=6$；
若 $v\ge2$，则 $E_\infty\ge10$。
其余正贡献至少4，所以仅余
$$
\boxed{
c=0,\quad u=v=1,\quad
\mu_h=(3,0,0,0),\quad\mu_1=(3,0,0),\quad
\mu_d=\mu_\infty=0,\quad
\kappa=15,\quad\chi=11.}
\tag{11}
$$
其整个来源是
$$
F=t+h_0+\sum_{n=1}^3
 \bigl(h_7(t)(t-1)Y\bigr)^n p_n(t),\qquad
\deg p_n\le n+1.
\tag{12}
$$
$H(0)$ 仍任意，不能在这一步删去 $h_0=0$。

$z=2$ 给 $\kappa\ge21$，不在这个小自交范围内。
故 $\kappa\le17$ 准确有二十一类必要包络。
按自交数分组，其数量为
$$
\begin{array}{c|rrrrrr}
\kappa&9&13&14&15&16&17\\ \hline
\text{类数}&1&3&3&4&3&7.
\end{array}
\tag{13}
$$
其中 $\kappa=15$ 的四类有一类为 (11)。

## 5. 四个剩余素数的整个非齐次矩阵

由 $\kappa\ge9$ 和 (4)，$h\ge23$。
若 $p\le407$，则 $h\le33$。
$12h+11$ 在这一范围内的素数恰为
$$
\boxed{(p,h)=(311,25),(347,28),(359,29),(383,31).}
\tag{14}
$$
其余值的分解为
$$
287=7\cdot41,\quad299=13\cdot23,\quad323=17\cdot19,\quad
335=5\cdot67,\quad371=7\cdot53,\quad
395=5\cdot79,\quad407=11\cdot37.
$$
所以实际剩余候选均有 $\kappa\le h-14\le17$，正好使用第4节。

每个几何类保其累计重数 $V_j^h,V_j^1,V_j^d,V_j^\infty$。
它的全部原正 charge 系数仍为
$$
F_n=h_7^{b_n}(t-1)^{c_n}d^{z_n}p_n,
$$
$$
\begin{aligned}
b_n&=\max\left(0,\max_{j\le4}
 \left\lceil\frac{V_j^h-3+n}{j}\right\rceil\right),\\
c_n&=\max\left(0,\max_{j\le3}
 \left\lceil\frac{V_j^1-3+n}{j}\right\rceil\right),\\
z_n&=\max\left(0,\max_{j\le2}
 \left\lceil\frac{V_j^d-n}{j}\right\rceil\right),\\
K_n&=\min\left(u+4n,\min_{j\le2}
 \left\lfloor\frac{ju+(4j+1)n-V_j^\infty}{j}\right\rfloor\right),\\
\deg p_n&\le K_n-2b_n-c_n-z_n .
\end{aligned}
\tag{15}
$$
这是原十九角各步帽的整个必要线性包络，保 $1\le n\le3$。
沿 $\rho$ 的列为
$$
t^j h_7^{b_n}(t-1)^{c_n}d^{z_n+n}\Theta^{17n},
$$
另加所有 $d^ct^j$、$0\le j<z$ 的常数 charge 列。
右端准确为 $-d^ct^z$，读取全部 $0\le i<h$ 行。

公共精确执行得到：

| p | h | $\kappa$ 上限 | 所有允许几何类数 | 相容类数 |
|---:|---:|---:|---:|---:|
| 311 | 25 | 11 | 1 | 0 |
| 347 | 28 | 14 | 7 | 0 |
| 359 | 29 | 15 | 11 | 0 |
| 383 | 31 | 17 | 21 | 0 |

共四十个类的出现，去除重复输入后是36个不同矩阵。
每一类都已经在完整非齐次系统中无解；
因此无需用 primitive、不可约或三个开条件再删解。
与 (9) 联合，证明定理。$\square$

producer 为核覆盖完整性还生成全部2541个十九角必要类，
并检查 $101<p\le407,\ p\equiv11\pmod{12}$ 的13个素数。
前九个素数没有满足强门的几何类，
其余四个恰是 (14)。
这只是完整复现方式；证明的有限段由 (10)—(15) 已压成上述二十一类，
没有把一个抽象维数或少量代表替代全部原来源。

## 6. 公开执行、完整证书及恢复说明

数学执行为本库公共 Actions：

- producer：[check-r797-original-r2-y-factor-b3.py](../scripts/check-r797-original-r2-y-factor-b3.py)；
- 参数：--max-order 64 --remaining-examples 20；
- source commit：abf0b529edcda0d85b8cc3d38b40bb392aaecccd；
- [run43739961915](https://github.com/Rogerhu12/math-research-public/actions/runs/43739961915)，job132890717650，成功；
- producer SHA256：bddaecd97411f33c564304944bd2cf6820d284d8cd444ba0beb8901dadf28cd7；
- 复用的 R788 exact helper SHA256：f729371aa6867a84e1a4de18abdcd6d2451987e7174809a0a19269631c68da0e；
- stdout 42182 bytes，SHA256：4eb229739fba2fa6f6e57583be02cab060287d656381a7f32dc7c12eedb40ce2。

正式输出逐格保全部56个 profile 的 masks、角帽、列数、
两个最大子式行范围与 hash、完整 gcd 因式和全 stream hash。
其中 uniform_gate_paid=true、largest_common_bad_prime=283、
largest_used_row=33、all_strong_b3_excluded=true；
有限报告的相容类和余类均为0。

完整 profile 报告 hash：
03b251d90a5b1d72e84830e9a620d563b3bfb7937328199c5a565f14ed79923e。
全部几何输入 hash：
3effac35a3fe26e4e37f712d07aac9b3ffbe6fe67e6d1c38514361a9fccf53ab。
全部有限矩阵结果 hash：
e4e3c07bb063f4d82623204f205513660ee5f11dcb9f19e9eb8ef9afa4f2d522。

第一次 run43739357371 的数学计算结束后，
因最终 stdout 超过既定59000字节限制而退出失败，不能作为完整发布证书。
随后仅压缩重复的报告字段，数学级数、原矩阵、枚举和消元算法未改；
上列成功 run 提供完整正式记录。
没有把可复算矩阵、RREF 或输出 JSON 写入仓库或 Release。

## 7. 精确关闭范围与继续的问题

本定理排除的是
$$
r=2,\quad b=b_0=3,\quad q(t,0)=0,\quad
\ell\in\{1,2\}
$$
在原强窗中的全部候选。
结合 R799 的 $q(t,0)\ne0$ 结论，得到：

**推论。** 在原 $r=2$ 强窗、$b_0>4k_{\rm carry}+2$ 及其余真实假设下，
无论 q 的常数 charge 是否为零，都不可能有 $b=b_0=3$。
因此任何这类原因子必须 $b\ge4$。

这没有把 $r\ge3,\ q(t,0)=0$ 的其他最低 charge 分支排除，
也没有给随 p 增长的 b 提供统一接触界。
原完整 $\mathcal W_D$ 的指定 Bockstein、同一个 R 的 normal、
两条十三行和下一精度仍需继续。

公开执行脚本的 scope 字段保留最初的 $\ell=1$ 标签。
本篇第1节已经逐项说明：被执行的系数、几何、p/h 关系及强门
都不含 $\ell$，所以将结论扩到 $\ell=2$ 不需要另跑数值，
也不转用任何 $\ell=1$ 独有的 lifting 公式。
主目标仍未完成。

依赖：
[R491](R491-valuated-source-factor-lifts-and-homogeneous-joint-obstruction.md)；
[R495](R495-fixed-angular-surface-and-full-triple-source-joint-image.md)；
[R550](R550-actual-ramification-koszul-quotient-and-full-third-kernel-image.md)；
[R797](R797-original-zero-constant-charge-moving-factor-and-complete-cubic-gates.md)；
[R799](R799-original-all-cubic-nonzero-constant-charge-windows-excluded.md)；
[R802](R802-original-moving-factor-return-and-unique-one-charge-exception.md)。
