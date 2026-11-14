# 真实 Poincaré 第一变量 Miller 搬运：恢复检查点

日期：2026-11-12。**状态：计算进行中；本笔记不宣称已有非形式纤维最终高度。** R141/R145 已给同一形式框架的完整 Hecke 相容局部值。当前计算将一个第一变量不在形式群的真实纤维搬到这个已知终点。

## 1. 固定对象和已经完成的终点

令 $B=B_{-4}$，$m=\#J(\mathbf F_{47})$，$Y=mB$。$m$ 和 $Y$ 都从已发布
`scripts/data/p41_formal47_multiplication_saved.json.gz` 读取，$m$ 为 304 位二进制整数，$m\equiv9\pmod{47}$。禁止手抄整数时漏掉中间的重复数字。

令 $f_0$ 是 R110 的固定典范截面，在 $\mathcal L=K_X+D$ 中有 $D_0=\operatorname{div}(f_0)$，次数 126。R112 的 $B$ 代表为 $A_B=E_B-D_0$。第二变量固定采用 R141/R145 的
$$
A_2(Y)=E_2(Y)-D_2=Z_2(t_2(Y))-Z_2,
$$
其中 $Z_2$ 是 54 个真实点。初始纤维为
$$
\mathcal P_{B,Y}=\operatorname{Norm}_{A_B}\mathcal O(A_2(Y)),
$$
输入元素为上述除子代表中的有理截面 $1$。因第二变量是形式点，而 $E_B,D_0$ 与这 54 个剩余圆盘分离，这个元素在双扩张模型上有合法整坐标。

已完成的形式终点为
$$
\Lambda^H(\sigma_{\rm new}(Y,Y))=4263370\pmod{47^4}
$$
（R145），同一框架的真正 Hecke 修正已由 R141 给出。

## 2. 每一步真实群律及符号

R121 的 AddFlip 从 $P,Q$ 算得 $R=-(P+Q)$。实际算法求出的三次截面 $f\in H^0(3\mathcal L)$ 满足
$$
\operatorname{div}(f)=E_P+E_Q+E_R.
$$
因此
$$
\psi=f/f_0^3,\qquad \operatorname{div}(\psi)=A_P+A_Q+A_R.
$$
三个范数框架的张量积在零纤维中给 $\psi(A_2(Y))$。若输入坐标为 $u_P,u_Q$，则实际负和坐标准确是
$$
\boxed{u_R=(u_Pu_Q\psi(A_2(Y)))^{-1}.}
$$
重复变量时用 $u_P^2$。实际 $-B$ 代表由 R117 的原始负点翻转重放，设其二次截面为 $a$，则
$$
\phi_B=a/f_0^2,\quad\operatorname{div}\phi_B=A_B+A_{-B},\quad
u_{-B}=\phi_B(A_2(Y))^{-1}.
$$
此处保留负号链，不能把 AddFlip 当普通正和。

新脚本的全部随机数消耗、选主元次序和矩阵规范与 R121 原长乘相同。每一步都比较已发布记录的完整点 SHA256 及秩字段；新增范数计算不消耗该随机数流。因而不是用任意另一个点代表替换既有路径。

## 3. 54 个移动点给出的准确范数

利用 R145 所有 820 点的三阶真实展开，在第二组参数 $t_2(Y)\in47R_4^{54}$ 处计算完整 $V_1,V_2,V_3$。若 $s$ 是 $k\mathcal L$ 的截面并在这些圆盘上为单位，则
$$
\left(s/f_0^k\right)(A_2(Y))
=\prod_{j=1}^{54}
\frac{s(Z_{2,j}(t_j))/f_0(Z_{2,j}(t_j))^k}
{s(Z_{2,j})/f_0(Z_{2,j})^k}.
$$
固定残余 72 次除子在正、负部分相消。这是实际除子范数，不是局部函数的任意插值。各截面本身是整幂级数，$t_j\in47R_4$，故三阶展开足够模 $47^4$；这里不使用尚未证明的高度尾项界。

所有 54 个分子和分母均逐点检验为单位，完整乘积虚部为零，且在 $1+47\mathbf Z_{47}$ 内。作为独立几何校准，把 R145 的实际 $\phi_1$ 放入该直接评价程序，准确得到
$$
\phi_1(A_2(Y))=1245877,
$$
与 R145 的两个 126 次限制代数及独立整数范数之比完全相同。

## 4. 实际终点换框已提前完成

R121 的最终除子是 $A_{\rm old}=E_{\rm old}-D_0$；R141/R145 第一组的形式代表是 $A_{\rm new}=E_1(Y)-D_1$。两有效除子 $E_{\rm old},E_1(Y)$ 都次数 126 且线性等价。

在旧理想内选截面 $s,g\in H^0(2\mathcal L-E_{\rm old})$，$s$ 在所有 820 评价点为单位。对新理想求 $(g/s)t\in V_2$ 的一维核，得到 $t\in H^0(2\mathcal L-E_1(Y))$。实际检查完整 73 维理想的等式
$$
(t/s)H^0(2\mathcal L-E_{\rm old})=H^0(2\mathcal L-E_1(Y)).
$$
这两个线性系无基点，因此
$$
\operatorname{div}(t/s)=E_1(Y)-E_{\rm old}.
$$
真正的度零代表过渡函数还包含基除子的变化：
$$
g_{\rm tr}=(t/s)(f_0/v_1),\qquad
\operatorname{div}g_{\rm tr}=A_{\rm new}-A_{\rm old}.
$$
已实际算得
$$
\boxed{g_{\rm tr}(A_2(Y))=2703817\pmod{47^4}.}
$$
因此旧到新坐标严格满足
$$
u_{\rm new}=u_{\rm old}/2703817.
$$
终点小证书 `scripts/data/p41_miller_endpoint47_certificate.json`，8945 bytes，SHA256
`d6f64fa615f033fdae79a6687cb0630ea377680b434676c9bb2f9dfff3b9d5c3`。
重做入口 `scripts/p41_miller_endpoint47.py`。这个终点计算已完成；完整 Miller 链仍运行中。

## 5. 最终应输出的数及其准确含义

令长链完成后的旧坐标为 $u_{\rm old}$。因为 $m$ 是 47 进单位，初始指定纤维元素的局部值应为
$$
\boxed{\Lambda^H(1_{A_B,A_2(Y)})
=m^{-1}\left(4263370+\log(u_{\rm old}/2703817)\right)
\pmod{47^4}.}
$$
它是 $\mathcal P_{B,Y}$ 中指定真实有理范数元素的局部值。它还不是 $\mathcal P_{B,B}$ 的值，也不是全局自高度或全局 QC 截面。第二变量的搬运、实际 CM 代表及规范全局截面比随后继续。

## 6. 已保存状态和恢复命令

稳定主源：`scripts/p41_poincare_miller47.py`，SHA256
`e9964f3da095976fe36c101e10edca8d144774423cd3a6d7dba55038fe1461d4`。

滚动文件：`/tmp/p41_poincare_miller47_rolling.json.gz`。每 5 位原子保存一次；必须读 JSON 中的 `bits_done`、`steps`、`point_sha256` 和 `torus_coordinate`，不要仅按文件名猜进度。

首个完整检查点为 5 位、5 个 AddFlip，121123 bytes，SHA256
`f795734acf831b55a8068d7e487e6bf75a243093a3d92d06c245d2c910a4f54d`，此时 $u=1200334$。五步用时约 157 秒；已经继续完整长链，原初会话号 66952。会话号不作为恢复依据。

当本文件及源码复制入课题后，在课题目录用：

```bash
cp scripts/data/p41_poincare_miller47_saved.json.gz /tmp/p41_poincare_miller47_rolling.json.gz
python scripts/p41_poincare_miller47.py --script-dir scripts \
  --local-height scripts/data/p41_hecke3_formal_height47_compact.json.gz \
  --checkpoint /tmp/p41_poincare_miller47_rolling.json.gz
```

若临时目录丢失，先按 R136、R141、R145 重建其可重建中间文件，再把最近已发布的固定 Miller 快照复制到该滚动路径。恢复会检查全部输入哈希和点哈希，然后从下一个二进制位开始。若没有固定快照，则从 $B$ 重新开始；不要冒认丢失进度。

本脚本只依赖既有 NumPy 路线，未引入新的 flint 求逆或改变 R121 的主元/随机路径。曾测量加速方案但没有采用它，以保持逐步原哈希比较。
