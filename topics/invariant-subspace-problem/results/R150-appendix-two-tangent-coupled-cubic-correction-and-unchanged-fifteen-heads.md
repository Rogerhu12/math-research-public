# R150 补篇：$s=2$ 切向耦合三次校正的真实增量与十五维首项保持

日期：2026-11-15。作者：Astra-ISP-789f / literature_audit；AI 辅助：GPT-6 Astra Pro。

## 1. 本次实际结论

在[纯三次高核唯一性](R150-appendix-two-pure-cubic-high-kernel-uniqueness-and-unchanged-first-heads.md)已经给出的两条真实高核候选上，本次完成第二条切向耦合列的原低行消元。固定原低块、首项强迫及两个新列分别记为
$$
B\in\mathbb Q^{1088\times585},\quad
C\in\mathbb Q^{1088\times22},\quad
C_{\rm cub},C_{\rm tan}\in\mathbb Q^{1088}.
$$
实际完整结果是
$$
\boxed{
\operatorname{rank}[B,C,C_{\rm cub},C_{\rm tan}]=592,\qquad
\dim\ker[B,C,C_{\rm cub},C_{\rm tan}]=17.}
\tag{1.1}
$$
相对于旧 $B$ 的完整 Schur 秩为九。向原二十二维常数首项的投影仍为十五维，与[最初低校正首项空间](R150-appendix-two-directed-fifteen-first-left-heads-and-zero-original-square-readings.md)完全相同。九个真实平方的读数仍全部为零。本次没有新增首项，也没有构造二阶 jet。

## 2. 新增列的完整原来源

在原常数方程
$$
F_e=\ell_e(z)+c\,r_e(z)+d\,q_e(z)+Q_e(z)
$$
中，令 $w$ 为 $\ker\mathcal L$ 的真实唯一弱方向。原第二条常数一次正常泛函可写为
$$
z\mapsto v,\qquad cz\mapsto a w,\qquad dz\mapsto b w.
$$
本次从同一已付常数核中实际提取并逐原十七式核得
$$
a=1,\qquad
b=-\frac{8109879152525169965}{28815675695304760788},
$$
$$
\ell_e(w)=0,\qquad
\ell_e(v)+a\,r_e(w)+b\,q_e(w)=0
\quad(1\le e\le17).
\tag{2.1}
$$

因此新增三次正常泛函准确为
$$
\nu_{\rm tan}(n_i n_j n_k)
=v_iw_jw_k+w_iv_jw_k+w_iw_jv_k,
$$
$$
\nu_{\rm tan}(cn_i n_j n_k)=a w_iw_jw_k,\qquad
\nu_{\rm tan}(dn_i n_j n_k)=b w_iw_jw_k,
\tag{2.2}
$$
其余坐标为零。原正常二次来源乘子对 (2.2) 的作用由 (2.1) 精确相消；原正常三次来源行因 $F_e$ 的纯常数部分为零而消失。程序又实际核验了全部 $5100$ 个高来源行。没有把 $g'(2)$ 置零，也没有删去任何原参数一阶项。

因为 $a\ne0$，它与无切向因子的纯三次泛函 $\nu_{\rm cub}=w^{\otimes3}$ 独立。两者的任意非零线性组合都有非零三次部分。若其原低列组合属于 $\operatorname{im}B$，则减去低校正后将得到具有三次部分的完整常数左核，违反已付的完整常数核全部支撑在正常次数至多一。因此
$$
\operatorname{rank}[B,C_{\rm cub},C_{\rm tan}]=585.
\tag{2.3}
$$
这保证本次零首项纤维仍恰为二维 $\ker B$。由 (1.1)，首项像维数为 $17-2=15$，与直接投影秩一致。

## 3. 全部原乘回、目标读数与范围

本次保留原全部 $6188$ 来源和真实 $s=2+t$ 参数。对十五个独立首项，逐项核验
$$
A_0^{\mathsf T}\lambda_0=0,\qquad
A_0^{\mathsf T}\lambda_1+A_1^{\mathsf T}\lambda_0=0
$$
的 $185640$ 个原有理坐标。所得首项矩阵与旧十五维首项矩阵具有相同逻辑身份。全部九个原目标仍是
$$
t_j=n_j^2,\qquad 2\le j\le10,
$$
其 $9\times15$ 一阶读数准确全零。

同头两个真实一阶代表的差属于完整常数左核，故其正常平方读数相同。更强地，本次所有相容代表的两条新增三次系数都必须为零：减去该首项的旧低支撑代表后，任何非零三次部分都会给出非法的高支撑常数核。

这一结论只穷尽本次由两条真高核构成的校正空间。尚未在本篇证明全部 $990$ 个三次正常坐标的高核恰为二维，更未覆盖正常次数四、五的校正。故不将低 Schur 的秩九称为完整第一连接的秩，也不由平方零读数断言原 $h_0$ 目标的局部成员性。

## 4. 精确增量和实际身份

旧二十三个实际右端、原 $583$ 阶单位及旧全部 $1088$ 行 Schur 均在同一任务内继承；只对 $C_{\rm tan}$ 新增一次单位方程求解和一列原 Schur。程序以重新生成的原右端矩阵逻辑 SHA 核父数据身份，再核保存解和 Schur 的全部继承坐标。父子检查点绑定不同，父数据保持只读。

实际运行：run $43736746064$，步骤 `two-tangent-coupled-cubic-first-jet-extension`，执行来源 `cb49fb2fa70a7fd1eba3e231649b015e2cfcef68`。数学用时 $12.236647931$ 秒，退出码零。

- [实际回执](../notes/r150-local-projection-session-789f/43736746064-two-tangent-coupled-cubic-first-jet-extension.json)记录所有原输入、系数、乘回与临时阶段身份。
- 实际源码 `notes/2026-11-15-r150-two-tangent-coupled-cubic-first-jet-extension-789f.py`，SHA256 为 `459538fc066f2df2372752c1a32ba33b6f2abe8f1ecd0ac44787cefd44214628`。
- 原始数学回执 $17596$ 字节，SHA256 为 `7b6849c6069982bc3bf2cc5c47c859b3670a9e78fff209f5153f29cb8de63194`。
- 新三次列的逻辑 SHA256 为 `fc25498e8fb70c05e79c0efcff7b91f44ab432d2dd11d60f90a6190edb482ce9`。
- 完整 $609\times17$ 核的逻辑 SHA256 为 `e38f3ebdbb694a420c2ec3ec461a091a57339ad496d722b47f1b66d16a9e8eeb`。
- 九平方零读数的逻辑 SHA256 仍为 `9985902de39ff67fb9a99762640bef9e7ec0b18ce2e567c211f8e7aee6e1f76b`。

没有上传可重算大矩阵，没有重做旧单位或旧二十三个右端。完整三次高核是否只含这两条方向，将由独立的真实有理上界与有限域秩下界比较决定；此处不预填该比较结果。
