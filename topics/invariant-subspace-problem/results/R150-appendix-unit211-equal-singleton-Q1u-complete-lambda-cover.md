# R150 unit211：h=k、Q=1−u 的完整 32 次 lambda 覆盖

日期：2026-11-27。会话：Astra-ISP-8542378f-20261127（AI-assisted GPT-6 Astra Pro）。

## 结论

当前原 h=k 碰撞图上，若 Q=1−u，则原点的 lambda 必须是以下三个完整 QQ 因子之一的零点：

$$
 C_2=3\lambda^2-2\lambda+1,
$$
$$
 C_6=24\lambda^6-72\lambda^5+96\lambda^4-76\lambda^3
       +39\lambda^2-12\lambda+2,
$$

以及下文完整给定的 C24。三个因子均由真实 QQ 因式分解及乘积返回，保留其全部复根。其首一化乘积为32次必要 lambda 覆盖。

在 Delta=0 的互补面上，只需要 C6、C24，并且每个 lambda 至多两个原 u；故该面至多60个不同的 (lambda,u) 候选。此时原自由 Gram 参数尚须返回。Delta≠0 的图也未排空，不能只从 lambda 覆盖声称原点数有限，更不能把32次覆盖当成单位证书。

旧 D≠0 值图中的 Q=1−u 排除不被用于本页。所有图、分母与原矩直接在 h=k、D=0 的原碰撞参数上构造。

## 1. 原作用域与支付来源

沿用[整个 Phi=0 碰撞排除](R150-appendix-unit211-equal-singleton-entire-Phi-zero-original-exclusion.md)及其先前完整等权、T0、J=Q 原排除。故当前 h=k 图可使用

$$
 A B\,S\,\lambda\,Q(1-Q)\,bc\,P_{02}\,(u-\ell)\,T_0\,(J-Q)\,\Phi\ne0,
 \qquad P_f=T_0(J-Q).
$$

其中 A、B、ell、xi、T、S、eta、w 及 Pc、NF、NC、Delta 等仍为此前原定义，不另选值根：

$$
 A=2\lambda^2-2\lambda+1,\quad
 B=4\lambda^3-6\lambda^2+3\lambda-1,\quad
 \xi=B/A,\quad\ell=A^3/B^2,\quad T=A^2/B.
$$

令 Q=1−u，完整原恒等式为

$$
 d=\rho^2=u,\quad
 T_0=(1-u)(2u-\ell),\quad
 J-Q=(1-u)(2u+\ell-1),
$$
$$
 \Phi=(1-u)(2u-\ell-3),\quad
 P_{02}=(1-u)\{-2u^2+3(\ell+1)u-2\ell\}.
$$

另有

$$
 \Delta=(1-u)^2D_s,
$$
$$
 D_s=(2u-\ell-3)\{3-4\lambda+(2u+\ell)\xi\eta\}
      -S\xi(2u-\ell)(2u+\ell-1).
 \tag{1}
$$

源对 (1) 的完整系数核验

$$
 [u^2]D_s=-4\xi^2\ne0. \tag{2}
$$

它不只是显示次数：分母无 u，分子 u² 系数除以同一分母准确等于 −4xi²。因此整个 Delta=0 面对 u 都是一个真实首一二次环境；lambda 首项退化不会损失此二次覆盖。

## 2. Delta=0：三个原相容式及整个 30 次覆盖

两条原仿射式的系数为

$$
 (P_c,P_f,bcQ\Phi),\qquad (N_C,N_F,bcQS\xi).
$$

定义

$$
 F=S\xi P_c-\Phi N_C,\qquad T_n=P_fN_C-P_cN_F.
$$

源完整乘回

$$
 P_fF+\Phi T_n+P_c\Delta=0,\qquad
 N_FF+S\xi T_n+N_C\Delta=0.
$$

当 Delta=0 时，原点必须同时满足 Delta=F=Tn=0；这里没有使用 Delta 逆。仅去掉已付原单位后，其完整 QQ[lambda,u] 分子为：

| 原相容式 | lambda 次数 | u 次数 | 项数 |
|---|---:|---:|---:|
| Delta | 12 | 2 | 39 |
| F | 16 | 3 | 68 |
| Tn | 19 | 3 | 80 |

固定 Delta/F、Delta/Tn、F/Tn 的 Sylvester 阶数为5、5、6。每条移位行重建回原多项式，保留其全部最高项为零的 lambda 纤维。三个原结式次数为65、67、99；只剥已付因子后的次数为30、33、47。

完整 QQ 扩展 Euclid 对三个必要投影给同一个30次 gcd，并真实因式分解为非零常数乘 C6 C24。所有除法、累计 Bézout 及因式乘积实际返回。

由 (2)，这30个 lambda 根每个至多两个原 u，因而不同 (lambda,u) 候选至多60。这个计数只针对原相容参数，不计尚自由的 f/t，也不替代完整 Gram 返回。

## 3. Delta≠0：完整八原行及 158 次投影 gcd

本图明确假设 Delta≠0。两条原仿射式准确、同点恢复

$$
 f=F/\Delta,\qquad t=T_n/(bcQ\Delta).
$$

源逐式乘回两个原仿射条件，以 H=1 直接重建全部原矩、E0/N0/P1/NV、两孤立原目标及八个原必要行。偶、奇提取来自两个实际 B/C 原式及 rho≠0。所得完整必要分子为：

| 原行 | lambda 次数 | u 次数 | 项数 |
|---|---:|---:|---:|
| E1 | 48 | 8 | 440 |
| EBe | 54 | 9 | 550 |
| EBo | 54 | 9 | 548 |
| N1 | 51 | 9 | 518 |
| NBe | 74 | 13 | 1049 |
| NBo | 70 | 12 | 922 |
| PBe | 85 | 15 | 1376 |
| PBo | 79 | 14 | 1199 |

全部分母逐因子返回既有原单位或本图 Delta；只在本图使用 Delta。固定原投影数据为：

| 原对 | 固定阶 | 原 lambda 次数 | 去已付因子后次数 |
|---|---:|---:|---:|
| E1/EBo | 17 | 818 | 404 |
| E1/N1 | 17 | 794 | 386 |
| EBo/N1 | 18 | 898 | 432 |
| E1/PBo | 22 | 1236 | 602 |

所有参数首项零均保留。它们的完整 QQ gcd 依次为404次、158次、158次、158次，最后精确分解为非零常数乘

$$
 C_2^4\,C_{24}^4\,C_6^9. \tag{3}
$$

实际规范首一158次 gcd 的升幂数组11914字节，SHA256为
8f9cb3e92df665b8ab76c688a0e9b97151993b7cb36fcb2305cb6acb78ff238e。
这里 (3) 的重数来自真实 QQ 投影，并不表示原点的局部长度。为覆盖其零集可取三个整因子的首一化乘积，但必须把所有原行返回其全部根。

## 4. 三个完整 QQ 因子的规范系数

C2、C6 已在开头写出。C24 按常数项至 lambda²⁴ 的整数系数为：

$$
\begin{aligned}
(&-18,\ 399,\ -4412,\ 32152,\ -171905,\ 710808,\\
&-2332482,\ 6112826,\ -12570078,\ 18848763,\ -14402138,\\
&-21172682,\ 111728893,\ -266613390,\ 460231700,\ -629475832,\\
&702614944,\ -645322096,\ 486216224,\ -296971456,\ 143911680,\\
&-53435136,\ 14348800,\ -2500608,\ 215040).
\end{aligned}
$$

规范升幂 JSON 摘要为：

| 因子 | 次数 | SHA256 |
|---|---:|---|
| C2 | 2 | 2397da705aa54a116fef13f791ee3c511214896361d31ef88af2c4985f5c063d |
| C6 | 6 | a006b796e0f5b5e8849c0ada704ccb5dc03a5e7c96912cf5ccfaaa5c23aef394 |
| C24 | 24 | b32c945a935f28d8985aae8898e317e00adb5eaba24bfe7d08811c81b79d5582 |

两个互补图独立返回同一 C6、C24。全部系数很小，已在随文小回执中保存，不需要重放原大结式才能开始原有限返回。

## 5. 实际执行

| 图 | 源 SHA256 | run / job | 驱动秒 | 峰值KiB | 内层退出 |
|---|---|---|---:|---:|---:|
| Delta=0 原相容 | 2298408cf56888d710f4a22d74026a81b2d900aca84541148459ea4eacfe6ab2 | 46018532882 / 140571845380 | 0.101131019 | 40688 | 0 |
| Delta≠0 全八原行 | 7eaa1987e85a9e1f9ac6752f496dc0ee9a9b31fcaf4c8c99f0d9d376423d095b | 46018529754 / 140571835908 | 11.665128284 | 69768 | 0 |

- [Delta=0 完整原相容源](../notes/2026-11-27-unit211-equal-singleton-Q1u-Delta-zero-original-compatibility-cover-8542.py)，blob e2d910f2451f9b4b8a9aacbfa4bd7a37708546a1，10593字节。
- [Delta≠0 八原行源](../notes/2026-11-27-unit211-equal-singleton-Q1u-nonzero-Delta-original-two-parameter-return-8542.py)，blob4c00d406964166eb5fa325430a1683bb33e3670a，12373字节。
- [两图实际小回执与全部小因子](../notes/2026-11-27-unit211-equal-singleton-Q1u-complete-lambda-cover-receipt-8542.json)。

两次真实部分克隆/pull后的提交均为2b5f45cb9d04b0e65a789ff0dee7cd035410e7a1；2026-11-27 14:44:05及14:44:07 UTC核两README无差异，使用Python3.12.14、python-flint0.9.0、单线程。

此后直接把 C2、C6、C24 的全部原有限代数返回到同一原系统，不重算这四个大投影。非恒定覆盖及全部原头零是后续输入，不是本篇的排除结论。
