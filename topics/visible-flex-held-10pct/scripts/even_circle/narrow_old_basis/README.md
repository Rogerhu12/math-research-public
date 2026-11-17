# 窄圆弧：旧控制基的已完成试验

依赖已发表 `../first_batch` 的原70源恢复、四重实际线性端口及基础helper。本包只增加三个执行源、八组线性/背景标量、两条已终态BVP记录和可移植恢复器。核心使用旧compact控制；新补集矩控制不属于本包。

`python prepare_narrow_runtime.py --repo REPO --dest NEW_SCRATCH_RUNTIME` 在仓库外再生端口、八组profile/chart，并逐值核对必要标量，写两条BVP replay命令；不重跑BVP。先运行直接jump命令生成λ0，再运行smallstep命令。chart、DN、checkpoint及位置数组只在运行目录生成，不进Git。

两个旧记录保存了底层原源变换hash，但没有顶层运行时driver hash。本包明确标为captured source，不伪造历史hash；冻结源码与当前实际执行文件逐字一致。解析控制Jac在固定材料角下推导精确核心的0/1/2jet，转换到计算角后包含自适应对流项v·δX_ψ；设计δ列仍为原中心差分。各方向差分的实测绝对误差与尺度保留，不称严格Jac证书。

八个profile各有不同物理g；homotopy改变核心目标及解出的δ，也不是同g加密。普通λ0可以小metric，圆化后全metric和Cartesian tensor增大，最终λ1触maxnodes。正性/几何域门及接受容差没有放宽。详细表见同名笔记。
