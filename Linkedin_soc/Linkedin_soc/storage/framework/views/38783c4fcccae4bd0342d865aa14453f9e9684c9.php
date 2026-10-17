
    <div class="page-wrap">
        <div class="card search-card p-4">
            <h3 class="sub-title"><?php echo e(get_phrase('Search Results')); ?></h3>
            <?php echo $__env->make('frontend.search.header', \Illuminate\Support\Arr::except(get_defined_vars(), ['__data', '__path']))->render(); ?>
        </div> <!-- Search Card End -->
        
        <div class="card people-card p-4 mt-4 mb-3">
            <h3 class="sub-title"><?php echo e(get_phrase('People')); ?></h3>
            <?php $__currentLoopData = $peoples; $__env->addLoop($__currentLoopData); foreach($__currentLoopData as $key=> $people): $__env->incrementLoopIndices(); $loop = $__env->getLastLoop(); ?>
            <?php
                if($people->id==auth()->user()->id){
                    continue;
                }
            ?>
            <div class="people-wrap mt-2">
                <div class="people-item d-flex mb-3 justify-content-between w-100">
                    <div class="d-flex align-items-center">
                        <!-- Avatar -->
                        <div class="avatar">
                            <a href="<?php echo e(route('user.profile.view',$people->id)); ?>"><img class="avatar-img rounded-circle w-100 user_image_show_on_modal" src="<?php echo e(get_user_image($people->photo,'optimized')); ?>" alt=""
                                    ></a>
                        </div>
                        <div class="avatar-info ms-2">
                            <h6 class="mb-1"><a href="<?php echo e(route('user.profile.view',$people->id)); ?>"><?php echo e($people->name); ?></a></h6>
                            <div class="activity-time small-text text-muted"><?php echo e(ellipsis($people->about,'30')); ?>

                            </div>
                        </div>
                    </div>
                    
                    <?php
                        $user_id = $people->id;
                        $friend = \App\Models\Friendships::where(function($query) use ($user_id){
                            $query->where('requester', auth()->user()->id);
                            $query->where('accepter', $user_id);
                        })
                        ->orWhere(function($query) use ($user_id) {
                            $query->where('accepter', auth()->user()->id);
                            $query->where('requester', $user_id);
                        })
                        ->count();

                        $friendAccepted = \App\Models\Friendships::where(function($query) use ($user_id){
                            $query->where('requester', auth()->user()->id);
                            $query->where('accepter', $user_id);
                            $query->where('is_accepted',1);
                        })
                        ->orWhere(function($query) use ($user_id) {
                            $query->where('accepter', auth()->user()->id);
                            $query->where('requester', $user_id);
                            $query->where('is_accepted',1);
                        })
                        ->count();
                        
                    ?>

                    <?php if($friend>0): ?>
                        <?php if($friendAccepted>0): ?>
                            <a href="#" class="btn btn-secondary align-self-start"><i class="fa-solid fa-user-group"></i> <?php echo e(get_phrase('Friend')); ?> </a>
                        <?php else: ?>
                            <a href="javascript:void(0)" onclick="ajaxAction('<?php echo route('user.unfriend',$people->id); ?>')" class="btn btn-primary align-self-start"><i class="fa-solid fa-xmark"></i> <?php echo e(get_phrase('Cancel')); ?></a>
                        <?php endif; ?>
                    <?php else: ?>   
                        <a href="javascript:void(0)" onclick="ajaxAction('<?php echo route('user.friend',$people->id); ?>')" class="btn btn-primary align-self-start"><i class="fa-solid fa-plus"></i> <?php echo e(get_phrase('Add Friend')); ?> </a>
                    <?php endif; ?>
                </div>
            </div>
            <?php endforeach; $__env->popLoop(); $loop = $__env->getLastLoop(); ?>
            
        </div> 
    </div>



<?php /**PATH C:\Users\Md Fuad Alam\Documents\New folder\Linkedin_socio\resources\views/frontend/search/people.blade.php ENDPATH**/ ?>