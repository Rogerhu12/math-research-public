# Phi H1 新原多项式输入：v 坐标、无头逆矩列与固定范数

日期：2026-11-28（Asia/Taipei）；会话 Astra-ISP-8542378f-20261127。

源文件：[完整自含源](2026-11-28-unit211-Phi-zero-H1-polynomial-v-source-scaled-matrices-fixed-norm-input-8542.py)。
Git blob 0ea9a132ac3d7d98739ddfdc5ef9f8e7393a0a23；
SHA-256 5f6ba628dd4a660a7cedc7bb338a7cebc9cdc1ac3b6d6958a36409cb578b00ef。
内部120秒、1GiB，零历史数据依赖。

仅在原旧物理D非零的Phi H1图使用。新坐标为 $v=Jf-G+bc\,z$，$bc$ 为已付原单位。
四原R/W/O/N1分别乘 $4M_nP_f^2,Q P_f^2,(1-Q)Q^2P_f^2,Q P_f^2$，
其中 $M_n=QM$；源码必须逐式完整乘回后才继续。
只按已付原单位去多项式内容。RWN三头的伴随矩阵构造 $hM_T,hM_v$，不倒置 $h$；
同点O行、真实乘法交换子及完整F6/NV乘上必要 $h$ 幂后返回固定三阶余子式。
所有 $h=0$ 原点保留。

固定lambda结式再取完整Q四次代数的规范数，是新同点必要多项式输入。
真实QQ正则Sylvester矩阵的最大赋权及完整dual给度数上界；只有首项模1009不消失才确认该QQ次数。
模范数和模gcd本身不排除QQ权纤维、不声称已识别P201。
源码不读取/恢复C256或C55系数，不重放旧Dixon或Gaussian门。

首次执行的全部结论以真实回执为准；本输入登记不声明范数已返、H1已排空或普通ISP完成。
