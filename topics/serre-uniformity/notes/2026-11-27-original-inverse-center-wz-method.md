# 原 inverse-center 序列的整指标 WZ 输入

日期：2026-11-27（Asia/Taipei）。会话：Astra-serre-24b8836b-20261126。

状态：公开 Actions run46015627853/job140561880424 已成功，完整证书及其一阶因式/原相邻单位见 [R1130](../results/R1130-original-inverse-center-recurrence-and-adjacent-unit.md)。
本输入不重做原 prime 窗口，也不以有限初值猜测递推。
原指定非零性与 Serre 主目标仍未由此证明。

## 原对象

对正奇整数 n，定义
$$
I_n=\sum_{j=0}^n\frac{(-1)^j\binom nj^2}{2j-n}.
$$
R1059、R1061 的原 $p=3n+2$、n 奇数情形满足
$S_n=(2/3)I_n\pmod p$，全部原 $q$/Raynaud/f_N 尺度仍沿该来源。
这个整 n 序列的统一步长二递推未在当前已成结果中登记；
它与 fixed-p 的短 D³/D⁶ 谱递推、Dixon 首除层是不同输入。

## 直接多项式证书，不由数值猜测

对有限阶数 $t=1,2,3$，置 $M=n+2t$，并在 $\mathbf Q(n)[k]$ 中定义
$$
Q(k)=\prod_{j=0}^t(2k-n-2j),\qquad
D(k)=\prod_{j=1}^t(2k-n-2j),
$$
$$
C_j(k)=
\left(\prod_{h=1}^{2(t-j)}
  \frac{n+2j+h-k}{n+2j+h}\right)^2.
$$
寻找 $\deg_k P\le5t-3$ 和 $a_0(n),\ldots,a_t(n)$ 使
$$
\begin{aligned}
&-(M-k)^2(2k-M)P(k+1)-k^2(2k-n)P(k)\\
&\qquad=\sum_{j=0}^t a_j(n)C_j(k)\frac{Q(k)}{2k-n-2j}.
\end{aligned}
\tag{W1}
$$
各项都是 k 多项式。程序只作这个系数矩阵在 $\mathbf Q(n)$ 上的
精确核运算；若找到，清完有理函数及数值分母，输出原始整数系数证书，
再次直接验证 (W1) 的残差为零。

令 $H_M(k)=(-1)^k\binom Mk^2$。因为
$$
\frac{H_M(k+1)}{H_M(k)}
=-\frac{(M-k)^2}{(k+1)^2},\quad
D(k+1)=\frac{Q(k)}{2k-M},\quad
D(k)=\frac{Q(k)}{2k-n},
$$
(W1) 恰等价于
$$
G(k+1)-G(k)=
\sum_{j=0}^t a_j(n)
 \frac{(-1)^k\binom{n+2j}{k}^2}{2k-n-2j},
\quad
G(k)=\frac{k^2P(n,k)}{D(k)}H_M(k).
\tag{W2}
$$
对正奇 n，D 在整数 k 没有零；$G(0)=G(M+1)=0$。
当 $n+2j<k\le M$，$C_j(k)$ 的分子含一个真正零因子，
所以对应较短二项式项正确消失。于是完整求和给
$$
\sum_{j=0}^t a_j(n)I_{n+2j}=0.
\tag{W3}
$$
清分母后的身份在所有正奇 n 上成立。
首系数的整数零点另报；在这样的 n 仍有身份，但不宣称可向前解递推。
专化到原 $p=3n+2\ge41$ 时 $n+2t<p$，显示的比值分母不含 p；
任何进一步使用首系数的可逆性仍需单独检查。

右端的 k 次数至多5t，左端对非零P的首项是
$-4\,\operatorname{lc}(P)k^{\deg P+3}$，所以所给次数范围是自然的有限范围。
本输入不先假定最小阶数，也不从递推本身宣称原 $S_n$ 非零。

## 精度、范围与执行

- 脚本只允许公开仓库 GitHub Actions；固定官方 SageMath 10.6 digest。
- 预算3600秒，预留90秒；只试阶数1、2、3，找到首个证书就停。
- 只额外审计六个正奇整指标的完整有限和作为边界转录核对；
  这不是 prime 扫描，也不作为统一证明的替代。
- 输出 source/request/README SHA、真实 run/source commit、有限矩阵大小、
  完整小证书与 canonical SHA、耗时和成功/失败状态；无 raw artifact。
- W1--W3 已由 root 与 o1_theta 独立纸核；运行所得具体系数已由 root/o1 亲读并与 canonical SHA 核验；后继纸面因式另获 o2 独核。

代码为 [original_inverse_center_wz.py](../scripts/original_inverse_center_wz.py)，
请求为 [original-inverse-center-wz-request.json](original-inverse-center-wz-request.json)。
公开 workflow 位于仓库根的 .github/workflows/serre-original-inverse-center-wz.yml，
只监听本请求文件，不触发其它课题。

形式和法的上游参考为 Petkovšek--Wilf--Zeilberger 的
[A=B 原书](https://www2.math.upenn.edu/~wilf/AeqB.pdf)；
本请求的具体有理因子与全部边界已在上文独立写出，
未使用某个软件返回值替代证书。
