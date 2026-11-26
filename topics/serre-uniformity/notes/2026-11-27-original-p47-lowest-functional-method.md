# 原 p=47 的实际 DQ(1-Q)λ 最低泛函：一次专用诊断

日期：2026-11-27。会话：Astra-serre-24b8836b-20261126。

## 唯一新输入与目的

只检查 $p=47,N=7,\ell=16$ 的原实际
$$
c=D\overline{\mathsf Q}(1-\overline{\mathsf Q})\lambda,\qquad
\lambda=-6(b+1)/(1-b^3)
$$
在 R1052 完整 CM 轮廓中的最低系数泛函。
保留全部 $\overline{\mathsf Q}^2$、coefficient-fixed Frobenius
和原全超奇异点配对。它不是 R1054 已完成的“最低列是否落核”测试，
不重新计算旧 $f_N,g_N$、旧 bare/norm 或已完成至 500000 的窗口。
公共 $q,j$ 的有限截断只是构造这个新实际输入所必需的中间值。

若 $c=0$，只记录此固定素数，不能反驳仅限 $p>C_*$ 的断言。
若 $c\ne0$ 且最低读数为零，也只是这个固定素数的真实一次项障碍。
若非零，只关闭这个新有限点；不能推全称单位性或 Serre 完成。

## 原算法与三种独立读数

在 $\mathbf F_{47}[b]$，取 R1037/R1045 的原 monic
$A=bQ(b^3)$，$r=1-b^3$、$f=r^{4N+2}$。
首先求 $\lambda$ 的唯一 degree $<\deg A$ 多项式代表。
对每个输入 $a$，实际 $\overline{\mathsf Q}$ 的第一种计算为
$$
\operatorname{quo}(f a(b^p),A^2)\pmod A.
$$
这里先构造完整 $a(b^p)$ 并真正除 $A^2$，
绝不先 mod $A$ 再除。最大多项式次数不超过 1077。

第二种计算先求
$$
T_a=f a(b^p)/A'\pmod A
$$
再读 $LT_a/(2rA')\pmod A$，
其中 $L=r\partial_b^2-4b^2\partial_b-9b/4$。
两读数必须一致，同时完整核
$$
\operatorname{rem}(f a(b^p),A^2)=T_aA'-T_a'A.
$$
求 $\mathsf Q\lambda,\mathsf Q^2\lambda,\mathsf Qv$，
并核 $\mathsf Qv=\mathsf Q\lambda-\mathsf Q^2\lambda$、
$D$ 反交换、new 投影和原 $B(c,v)=0$。

最终最低泛函使用三种方式：

1. R1052 的准确 $r$-系数：
   $-3^{\ell-1}A(1)^{-1}[r^{\ell-1}]
   T_c((1-r)^{1/3})(1-r)^{-5/3}j^{-3}$。
2. 直接反演同一 $Z=-r(q/j)^3/3$，
   再从完整 $(T_c/A)(B_{\rm CM}(Z))$ 读取 $Z^{\ell-1}$。
3. 真正形成 $L_{\rm CM}=\operatorname{PP}_{b=1}(Z_b'/Z^\ell)$，
   核其简单极部为零，在 $\mathbf F_p[b]/A$ 中读取完整 $S$ 配对
   $-[b^{\deg A-1}](T_cL_{\rm CM}\bmod A)$。
   这个 Lagrange 系数等式同时包含全部 $A$-根，不抽样某几个点。

只用 $j_0,\ldots,j_{15}$，不请求首次共振的 $j_{16}$。
另记录实际完整约化轮廓的非零项数量和最低非零 $w$ 次数，
明确这是模 $p$ 读数，不是特征零最低次数。

## 公开执行、预算和回执

仅在新专用公开 workflow “Serre original p47 lowest functional”
执行一次。数学前检查真实 Actions、仓库、workflow 名称、
固定请求以及两份 README、程序、方法和证明来源的 SHA-256。
纯 Python 有限域多项式，无新增依赖。

单 job 数学总预算 **120 秒**，SIGALRM 和循环预算同时限制；
workflow 五分钟只覆盖环境准备外限，不作为数学预算。
stdout 只打印 CONTRACT、SUMMARY、OUTPUT_RECEIPT、BUDGET_RECEIPT，
记录三个准确读数、输入/实际向量/泛函来源哈希及真实 source commit/run。
不写 raw 数组、artifact 或 Release；失败不作数学结论。

代码由 global_route 给出，root 逐式核了完整 quotient 与 differential
读法、原系数固定约定、参数反演末端精度和全 $S$ 配对。
代码未在本地或会话内执行；只做文本、哈希和 Git 操作。
数学结果必须等待真实公开 job 回执。
