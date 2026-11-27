# R150：h=k、b=c 原碰撞的 96 次 QQ 覆盖与四个完整常数因子

日期：2026-11-27（Asia/Taipei）。会话：Astra-ISP-8542378f-20261127。AI-assisted GPT-6 Astra Pro。

## 1. 精确范围与结论

本稿处理[权不变量八原式](R150-appendix-unit211-equal-singleton-invariant-weight-full-original-system.md)中的
$$
h=k\ne1,\qquad b=c,\qquad \Delta\ne0.
$$
在本图物理 D=0；不借用此前 D≠0 原值图的等权排除。由 rho≠0，等权准确等价于 u=ell，故
$$
\ell=A^3/B^2,\quad b=c=\ell/2,\quad u=\ell,\quad
A=2\lambda^2-2\lambda+1,\quad B=4\lambda^3-6\lambda^2+3\lambda-1.
$$
唯一自由权参数为 Q，rho²=1−Q；两种 rho 均保持。

本次实际生成该整面全部八条原条件，并完成四个固定 QQ 结式及其完整一元 Bézout 返回。每个原点的 lambda 必满足一个首一 96 次 QQ 多项式。其全部不同因子只有次数 2、10、2、20 四类，总不同因子次数 34。下面给出全部精确因子。

这是有限 lambda 覆盖，尚未声明各纤维的原 Q 条件为空。Delta=0 图和一般不等权图另行保留。

## 2. 从同一完整 Gram 得到整面的八式

在父稿公式中先令 u=ell，再重建同一 H=bcDelta 缩放原 Gram。没有从一个较大计算输出中任意选择一个数值点。原三个 moment、E0、N0、双点 P1、N4(V) 和两单点正确目标均实际返回。原 B、C 两行共同保证合法偶奇分拆。

所有原系数分母只含 A、B、Q、1−Q；清分母后只剥原物理单位。除父稿单位外，本次还复用已完成的整个 S=0 排除，因此
$$
S=\frac{(2\lambda-1)(2\lambda^2-1)}A
$$
在实际余图为单位。lambda=1/2 的排除含原第五列物理秩论证，不能把它改称裸抽象理想已返回 1。

完整原行的 primitive 次数 (lambda,Q) 和项数如下：

| 原行 | 次数 | 项数 |
|---|---|---:|
| E1 | (42,6) | 285 |
| EBe | (42,6) | 285 |
| EBo | (34,5) | 201 |
| N1 | (40,6) | 273 |
| NBe | (63,8) | 556 |
| NBo | (63,7) | 490 |
| PBe | (67,8) | 592 |
| PBo | (63,9) | 614 |

每行的完整 QQ 因式分解也实际乘回，各 primitive 只有一个正次数因子。八式总 gcd 为 1，但这个多变量 gcd 事实没有被用来宣称没有孤立原点。

本次剥除按 gcd 循环逐次乘回；循环次数不自动等于一个完整原单位多项式的幂次。全部准确分子和剥除来源保附带小凭据及冻结源。

## 3. 四个固定原 Q 结式

令上述 primitive 原行分别为 C_name。计算
$$
R_1=\operatorname{Res}_Q(C_{EBo},C_{N1}),\quad
R_2=\operatorname{Res}_Q(C_{EBo},C_{E1}),
$$
$$
R_3=\operatorname{Res}_Q(C_{EBo},C_{EBe}),\quad
R_4=\operatorname{Res}_Q(C_{EBo},C_{NBo}).
$$
源码按各自固定 Q 次数完整生成 Sylvester 行，并逐行核对其是同一原输入的 Q 移位。然后实际求完整 QQ 结式；未在参数点处先降阶。

| 两原输入 | 固定阶数 | 原结式 lambda 次数 | 只剥真实单位后的次数 |
|---|---:|---:|---:|
| EBo,N1 | 11 | 370 | 201 |
| EBo,E1 | 11 | 381 | 212 |
| EBo,EBe | 11 | 380 | 216 |
| EBo,NBo | 12 | 510 | 285 |

对结式仅除那些实际整除 A、B、lambda、P02 或 S 的纯 lambda 因子。每次都完整乘回；它们在同一原图非零，不引入新的头系数单位。原 Q 次数在特殊 lambda 处降低，甚至个别整条原行变成零，仍给同一个固定 Sylvester 的幂列核向量；没有遗漏这些纤维。

记剥除后的四个多项式为 r_i。每个实际原点必须有 r_i(lambda)=0。对它们实际扩展 Euclid，逐次得到首一 gcd 次数
$$
201,\quad98,\quad98,\quad96.
$$
每次都完整核验
$$
\sum_{i\le j}a_{j,i}r_i=g_j
$$
的全部 QQ 系数。这是必要一元覆盖的真实返回；没有声称未输出的完整原多变量余子式证书。

最终首一 F96 的规范系数 JSON 为 4041 字节，SHA256
c1d642643c9ce69974495d5803f912166a76fb3672f9d8a94a1994dcb9fd89c6。
其全部系数由源再生，并在小凭据中保留。

## 4. 完整 QQ 因子

令
$$
\phi_{2a}=3\lambda^2-2\lambda+1,\qquad
\phi_{2b}=\lambda^2+\lambda-1.
$$
按常数到最高次列出其余两个整数多项式：
$$
\phi_{10}:\quad
(1,-7,30,-90,208,-379,529,-548,380,-168,48),
$$
$$
\begin{aligned}
\phi_{20}:\quad(&-3,52,-392,1470,-414,-29126,199932,-829326,2534173,\\
&-6080694,11783324,-18678024,24316352,-25940944,22500320,\\
&-15651136,8547840,-3547392,1058304,-202752,18432).
\end{aligned}
$$
实际完整因式乘回为
$$
F_{96}
=\frac{\phi_{2a}\phi_{10}\phi_{2b}^{\,2}\phi_{20}^{\,4}}
{\operatorname{LC}(\phi_{2a}\phi_{10}\phi_{2b}^{\,2}\phi_{20}^{\,4})}.
$$
故所有原 lambda 都在这四个完整常数纤维中。不同根覆盖只需其平方自由支持，次数 34；重数仍在原 F96 中完整保留。

后续在每个整个 QQ[lambda]/phi 商中返回原八式，不挑一个嵌入或数值根。即使采用的常数因子有非单位系数，也必须真 Bézout 作逆或完整分成两支；不能删除一个范数零分量。仍须保原 Q、1−Q、P02、Delta 等实际单位和全部 Q 头退化。

## 5. 实际执行

[冻结源](../notes/2026-11-27-unit211-equal-singleton-equal-weight-original-Delta-nonzero-face-8542.py)：
blob 8d6cb00f75b2110c5a42fffce19b43843c67a99c，
SHA256 ba8a23067ebd287bfcbe2e4f2eb08dfa423cafc72055f7481985b77dbcda3018。

- run46004053596/job140522654789，内层 exit0。
- 源 1.390871392 秒；驱动 1.469637955 秒；RSS 47168 KiB。
- stdout 64915 字节，SHA256 60edc3813875c263aeccc94b2d316b72f68f56932351ecc4ddd4acecccd3d1b2。
- 实际 main afa5e0c81f5702e4007238ce45b3b0c54f98e0a2。
- 13:05:24.208328 UTC 真实 pull 后两 README 无变化。

[小凭据](../notes/2026-11-27-unit211-equal-singleton-equal-weight-96-cover-receipt-8542.json)保完整执行身份、八式大小、四个完整结式摘要、原单位剥除、全部最终因子与 F96 系数。可再生的较大中间多项式只保 SHA。

本稿没有关闭 Delta=0、全部 h=k 或普通 ISP。四个精确常数域已送入独立的完整原 QQ 返回。
