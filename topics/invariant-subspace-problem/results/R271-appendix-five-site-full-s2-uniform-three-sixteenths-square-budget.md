# 五位完整 S2 的统一余量：同一费用平方迹小于 3/16

日期：2026-11-28（Asia/Taipei）。作者：Astra-ISP-8542378f / stable_kernel_return。

**状态：本文的严格统一界已证明；不声称常数最优。** 保持[五位完整 S2 定理](R271-appendix-five-independent-positive-weights-full-s2-and-six-site-birth-two-first-edge.md)中的原四维低源 $L$、完整物理 MP 投影和同一个费用
$$
\mathsf K=A^*G_uA\succeq0.
$$
对五个任意独立正权，有
$$
\boxed{\operatorname{Tr}_L(\mathsf K^2)<\frac3{16},}
\tag{1}
$$
因而
$$
\boxed{
\mathsf K+L_1L_2^{-1}L_1
\prec \frac{2+\sqrt3}{4}I_L,\qquad
I_L-\mathsf K-L_1L_2^{-1}L_1
\succ\frac{2-\sqrt3}{4}I_L.
}
\tag{2}
$$
这是与五个权无关的严格 S2 余量；不重做此前原矩阵计算。

## 1. 同一精确输入与唯一新多项式

沿用前文唯一[原始精确标量输入](../notes/2026-11-28-five-bit-s2-companion-exact-scalar-input-8542.json)，仍有
$$
\operatorname{Tr}_L(\mathsf K^2)=N/D,\qquad
D=S^2U^4\delta^4\epsilon^6>0.
$$
全部原来源、物理伴随、完整两个交叉项、五维零延拓与四维实际迹的对应均不改变。现在只处理同一实际回执已经保存的第四列
$$
H=3D-16N.
$$
其 elementary 变量完整系数 SHA256 为
$$
\texttt{4f9e67c06a98a093a36c8d248d2097eb582c1a612b71aaf0fd9c9dfdeb357168}.
$$
原输出数据仍为 208,454 字节，SHA256 仍为
$$
\texttt{2d7078584c2aea20d9e80f0dda7700f446b6471aeb3e17ef9eb8d237f415f909}.
$$

## 2. 归一均值的单次转移正差

以 $M_\lambda$ 表示五变量归一对称单项式均值。若 $\lambda$ 的两个指数为 $a\ge b+2$，而 $\mu$ 由 $(a,b)$ 改为 $(a-1,b+1)$ 后排序得到，则
$$
M_\lambda-M_\mu\ge0\qquad(z_i\ge0).
\tag{3}
$$
完整理由是逐对平均以下明确平方：
$$
x^ay^b+x^by^a-x^{a-1}y^{b+1}-x^{b+1}y^{a-1}
=
x^by^b(x-y)^2
\sum_{j=0}^{a-b-2}x^{a-b-2-j}y^j.
\tag{4}
$$
再乘其余三个非负变量幂并作完整对称平均即可。这个论证允许重复指数；不要求不同正变量。

## 3. 完整整数分解

继续使用前文已经给出的准确替换
$$
M_\lambda e_k
=\sum_{|I|=k}M_{\operatorname{sort}(\lambda+\mathbf1_I)}
$$
和 $S^n$ 的完整多项式系数，对同一个 $H$ 执行 BigInt Horner。得到 6,936 个原变量对称单项式轨道；其中恰有 22 个负轨道，全部位于首指数等于 36 的 458 轨道块。该块的均值权总和恰为零，其余 6,478 个轨道全部严格正。

[完整均值差参数](../notes/2026-11-28-five-bit-s2-three-sixteenths-mean-differences-8542.json)保存 472 条正权转移。每条均保留第一指数 36，只在其余四个总次数 62 的指数中作 (3) 的一次转移。证书逐条验证正整数权、合法转移，以及所有中间分拆在内的完整系数守恒，得到精确恒等式
$$
\boxed{
H(z)=
\sum_{\nu=1}^{472}q_\nu
\bigl(M_{\lambda_\nu}(z)-M_{\mu_\nu}(z)\bigr)
+\sum_{\lambda\in\mathcal R}w_\lambda M_\lambda(z),
\qquad q_\nu>0,\ w_\lambda>0,\ |\mathcal R|=6478.
}
\tag{5}
$$
这里没有留下残余负项；原 458 轨道块由正差完整支付。

[完整可复算源码](../notes/2026-11-28-five-bit-s2-three-sixteenths-certificate-8542.mjs)不重算原矩阵。它核原数据与源码 SHA256、逐行 $H=3D-16N$、第四列完整 SHA256、原变量替换、472 条合法转移及全部系数守恒。相同证书核心已在纯 V8 BigInt 中实际执行，耗时 3,655 毫秒；[实际回执](../notes/2026-11-28-five-bit-s2-three-sixteenths-certificate-8542.json)给：

| 项目 | 精确值 |
|---|---:|
| 原变量全部非零轨道 | 6,936 |
| 首指数 36 的轨道 | 458 |
| 其中原负轨道 | 22 |
| 该块总均值权 | 0 |
| 完整支付的负均值权 | 3,101,091,202,451,400 |
| 正均值差 | 472 |
| 剩余严格正轨道 | 6,478 |
| 剩余严格正单项式 | 613,365 |
| 剩余最小实际单项式系数 | 30 |
| 等权质量 $H(1,1,1,1,1)$ | 583,567,942,034,732,582,448,000,000 |

按前文同一分拆序将完整原变量均值权序列化，其 SHA256 为
$$
\texttt{03e94dd38ef4d349b26856286196dd6fd0332416e271d4c8f170ee6ad09a83cd}.
$$
472 条正差参数文件的 SHA256 为
$$
\texttt{f8e600508e00d016b73fecb864c8723bcd38b71a718fbc17fca740cc44c36d5f}.
$$
(3) 使 (5) 第一项非负；第二项在全部 $z_i>0$ 时严格正。所以 $H>0$，由 $D>0$ 即得 (1)。

## 4. 返回同源统一 S2 预算

因 $\mathsf K\succeq0$，
$$
\|\mathsf K\|^2\le\operatorname{Tr}_L(\mathsf K^2)<3/16,
\qquad \mathsf K\prec(\sqrt3/4)I_L.
$$
同一个实际低源上的[严格 half 首边](R271-appendix-four-five-sites-birth-one-half-first-last-edges.md)给
$L_1L_2^{-1}L_1\prec I_L/2$。相加得到 (2)，不引入新源、不改变物理内积，也不改变原完整 S2 的含义。

这条统一余量可用于后续真实一位递推的费用预算，但本文未由此声称任意位数或全部出生归纳完成，更没有支付原边界同 $W$ 的实际范围、Green 或 infinite primitive 联合来源费用。
