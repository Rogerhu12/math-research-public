# R150：全余 W 的规范三原行、完整理想等价及越过 C13 零面的 S 一次式

会话：Astra-ISP-8542378f-20261127。日期：2026-11-28（Asia/Taipei）。

**结论。** 当前 W 原域中，三条原 F 一次方程可以通过整个已付权矩阵变换为
$$
F-F_p,\qquad p_2(S),\qquad p_3(S),
$$
并且正反两个方向都是准确的原理想身份。p2 对 S 至多二次，p3 至多三次。连同原首一 q3，得到一对新的同 S 二次式，及一条全域必要的 S 一次式。

新一次式在旧 C13=0 的整个纤维上同样成立。它的头与常数对 lambda 的次数仍为 4、5，但权分次分别降为 (27,37)、(28,37)，两系数的完整共同因子为 1。这个 gcd 结论不代表没有同时零点；所有新头零面和全部其它原条件继续保留。

## 1. 使用整矩阵，得到完整正反身份

沿用[整个 G36 排除与共同 F 恢复](R150-appendix-unit211-W-G36-entire-original-exclusion-and-global-F-recovery.md)。令
$$
R_i=A_i(S)+B_i(S)F,\qquad
B_i(S)=c_i+\alpha_i\lambda+\beta_iS,
$$
依次来自原 E1、EBe、N1。它们的原首一约化、清分母和已付内容已由同一冻结输入固定。权矩阵
$$
\mathcal B=
\begin{pmatrix}
c_0&\alpha_0&\beta_0\\
c_1&\alpha_1&\beta_1\\
c_2&\alpha_2&\beta_2
\end{pmatrix}
$$
的行列式 DeltaB 已在整个当前 W 支支付。此次使用实际伴随矩阵构造 U=B逆，并把 U B=I、B U=I 的全部十八个系数乘积逐项返回。完整逆矩阵规范编码 42057 字节，SHA256
197ccce479a57c61931ac5f10800f8aa77566e3de901314ac84107e64edc405a。

定义
$$
\mathcal A_j=\sum_iU_{ji}A_i,\qquad
\mathcal R_j=\sum_iU_{ji}R_i.
$$
源码完整核回
$$
\mathcal R_0=F+\mathcal A_0,\quad
\mathcal R_1=\lambda F+\mathcal A_1,\quad
\mathcal R_2=SF+\mathcal A_2,\qquad
\mathcal A_0=-F_p.
\tag{1}
$$
各 Acal_j 对 S 都至多二次。所有逆只含当前已付权因子，没有 C13、某个单独 Bi、几何首项或物理 D 的逆。

置
$$
p_2=\mathcal A_1+\lambda F_p,\qquad
p_3=\mathcal A_2+SF_p.
\tag{2}
$$
实际的前向原组合为
$$
F-F_p=\mathcal R_0,\quad
p_2=\mathcal R_1-\lambda\mathcal R_0,\quad
p_3=\mathcal R_2-S\mathcal R_0.
\tag{3}
$$
反向则完整返回
$$
R_i=c_i(F-F_p)
+\alpha_i\bigl(\lambda(F-F_p)+p_2\bigr)
+\beta_i\bigl(S(F-F_p)+p_3\bigr).
\tag{4}
$$
因此在当前系数局部化环的多项式环中，准确地有
$$
(R_0,R_1,R_2)=(F-F_p,p_2,p_3).
\tag{5}
$$
这不是只在某个选择的两个行或某个 Bi 非零补图上的恢复；整个 C13=0 权纤维也在 (1)–(5) 内。

## 2. 原首一三次下的两条新二次

共同环境仍是已付的
$$
q_F(F,S)=F^2+p(S)F+q(S),\qquad
q_3(S)=S^3+\beta_2S^2+\beta_1S+\beta_0.
$$
p2 对 S 的实际次数为 2，p3 为 3。按 q3 作首一除法，实际核回
$$
p_3=g+\eta q_3,\qquad \deg_Sg\le2,
\tag{6}
$$
其中 eta 为标量系数，不对它求逆。令 f=p2。于是连同 q3，(5) 准确等价于
$$
(F-F_p,f,g,q_3).
$$
仍须保留 qF(Fp,S) 以及每条其它原式的同点返回；不能把 qF 在旧环境约成零后删除，也不能用这两条必要二次取代完整原 N/P。

三条 Acal 的有理系数分子最大分次为 (13,17,2)、(15,20,2)、(16,21,2)。p2、p3 的规范编码分别为 39387、42501 字节，SHA256 为
81a96789814589898747cbb9fa7f69623a8f5771db0af0790ea1f5b5c487fcd0、
a49018ea84248e970f3a278fc866f9f4d029de239574dd805bf4648e925db636。

分别清除已付分母并仅剥已付内容，写
$$
f=f_0+f_1S+f_2S^2,\qquad
g=g_0+g_1S+g_2S^2.
$$
实际的完整系数分次如下。

| 系数 | 分次(e,k,lambda) | 项数 |
|---|---:|---:|
| f0 | (15,20,3) | 849 |
| f1 | (14,20,2) | 571 |
| f2 | (13,20,1) | 341 |
| g0 | (19,25,4) | 1721 |
| g1 | (18,25,3) | 1278 |
| g2 | (17,25,2) | 850 |

每个规范化系数均实际乘回原有理系数。完整新六系数输入 131155 字节，SHA256
8824b3eaad421969e695d9e70ba279f39dbce2a55144853daa16ee306e69ba59；
其确定性定义为本源对 (2)、(6) 的逐系数清理，完整实际载荷在下列原 job 的 stdout 中。本稿只归档源、参数定义及字节/SHA，不发布参数片或 manifest。后续 Actions 如需准确系数，可直接读取该原 job 日志到临时文件，或从冻结源的必要构造前缀取得，不经工具分片或编码搬运可重算数据。

## 3. 全域新 S 一次式，保全部新首项零点

直接取
$$
g_2f-f_2g=(g_2f_1-f_2g_1)S+(g_2f_0-f_2g_0).
\tag{7}
$$
源码在完整原多项式中核回 (7)，没有倒置 f2、g2。仅剥已付内容后得到
$$
L_1^{\rm can}S+L_0^{\rm can}=0.
$$

| 系数 | 分次(e,k,lambda) | 总次数 | 项数 | 规范编码字节 | SHA256 |
|---|---:|---:|---:|---:|---|
| L1can | (27,37,4) | 55 | 3490 | 101374 | b8721fda0d203c3f9e9475eab289bec52642f68f4728dc1b0be80d68b6e4fdcd |
| L0can | (28,37,5) | 56 | 4411 | 129895 | 64c434f1c147d6bb772cc15bd1ef3571cd2c0db89b32c520dfdf80856c0ccba7 |

两多项式完整 gcd 的规范结果为 1。这里只登记准确共同因子，绝不由多变量 gcd 为 1 推出没有共同零点。L1can=0 的全部原点仍须满足 L0can=0 和其它原条件；没有在当前原系统中支付 L1can。

完整新一次式精确输入 231505 字节，SHA256
88e928b3d2f28b20f71f1fc9f34cdd0642661b47b09b5c87e0d7e8dcce301935；
其完整确定性定义是 (7) 连同源码中已付内容清理。实际完整载荷位于原 job stdout，参数字节/SHA 已核对；不作为新数据片或 manifest 发布。

## 4. 与旧 C13 因子的准确关系及其作用域

[两原均值旧一次式](R150-appendix-unit211-W-two-original-mean-S-affine-and-fixed-resultants.md)中的系数记为 L0old、L1old，其 13 项纯权共同因子是
$$
\begin{aligned}
C_{13}={}&e^3k^4-e^2(6k^3+2k^4+k^5/2)\\
&+e(32k+48k^2+20k^3+13k^4/4)
-32-40k-14k^2-k^3+k^4/4.
\end{aligned}
$$
在本次新原组合已经完成后，只读取两次既成日志中的精确输入，V8 BigInt 有理运算实际逐项核回
$$
L_j^{\rm old}=-32C_{13}L_j^{\rm can},\qquad j=0,1.
\tag{8}
$$
L0 的全部 5488 个旧系数、L1 的全部 4362 个旧系数均返回。该额外小计算用时 262 毫秒，没有再生成旧原行、cofactor 或结式；源为[准确输入乘积核回](../notes/2026-11-28-unit211-W-canonical-affine-C13-original-input-identity-8542.js)，SHA256
1b62d59283d1a836ff1c5ce69ff8c45a753ebd620a6c085a9c41b3004f8e8135。

(8) 本身不允许在 C13=0 上取消 C13。全域新一次式的合法性来自独立的原身份 (1)–(7)，所以旧 C13 零面已经有同样的新必要一次式，但本文仍不宣称该零面排空或 C13 已付。式 (8) 只说明两个准确规范输入的关系。

## 5. 唯一实际运行与保存边界

源：[2026-11-28-unit211-W-canonical-three-original-F-rows-and-S-affine-8542.py](../notes/2026-11-28-unit211-W-canonical-three-original-F-rows-and-S-affine-8542.py)。

- blob 4086040667b731468310492b13bb8e1b0bf163f8；
- SHA256 a8cbbc7c4300b3c9d5ad9839daf6e487e0107e68a951d0f59523d4955b46c265；
- run/job 46058018197 / 140705155517；
- source commit 26e15682cce2291ca7cb1667d81231a5aef11178；
- 原最终数学标记 2.747312937 秒；驱动 2.786010989 秒；
- 内层 exit 0，峰值 72116 KiB，预算 180 秒、4 GiB；
- stdout 176489 字节，SHA256 68a945e4a3af4837a607f8806c36edb95307ae0651824d99920a47089c0a6afa。

真实 pull 于 2026-11-27 19:37:49.427087 UTC，前后均为上列 source commit，根与课题 README 均未变。

源只再生已冻结 8430 的共同 F 构造前缀，未重跑原十二行门、旧 NS/NV cofactor、旧大结式或任何已闭分支。本稿没有倒置物理 D；其完整原系统的等价仍限于前文沿用的 W 已付域，不能外推到 h_U=k_U 碰撞图。

[小回执](../notes/2026-11-28-unit211-W-canonical-three-original-F-rows-and-S-affine-receipt-8542.json)保留全部实际数学标记、原迹 SHA、参数定义/字节/SHA、原 run 标识和额外的 (8) 有理乘回记录。本次只归档确定性源及小回执，不归档可重算系数、参数片、manifest 或原大矩阵缓存。

整个 W 的其余原约束继续开放，普通 Hilbert ISP 未完成。
