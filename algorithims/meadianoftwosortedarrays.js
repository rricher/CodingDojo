// /**
//  * @param {number[]} nums1
//  * @param {number[]} nums2
//  * @return {number}
//  */

function findMedianSortedArrays(nums1, nums2) {
    var mead = 0;
    var meads = [];
    if (nums1.length == 0) {
        meads = nums2;
    } else if (nums2.length == 0){
        meads = nums1;
    } else {
        for (var i=0; i<nums1.length;i++) {
            for(var j=0; j<nums2.length;j++) {
                if (nums2[j] < nums1[i] && j < nums2.length -1) {
                    meads.push(nums2[j]);
                } else if (i== nums1.length -1 && nums2[j] < nums1[i] && j == nums2.length -1) {
                    meads.push(nums2[j]);
                    meads.push(nums1[i]);
                } else if (i == (nums1.length -1) && nums2[j] >= nums1[i] && j == 0) {
                    meads.push(nums1[i]);
                    meads.push(nums2[j]);
                } else if (i == (nums1.length -1) && nums2[j] >= nums1[i] && j > 0) {
                    meads.push(nums2[j]);                
                } else {
                    break;
                }
            }
            if (i != nums1.length -1) {
                meads.push(nums1[i]);    
            }    
        }
    }
    return meads;
    // if (meads.length % 2 == 0) {
    //     mead = (meads[meads.length/2] + meads[meads.length/2 - 1]) / 2;
    // } else {
    //     mead = meads[meads.length / 2 -.5];
    // }
    // return mead;
};
    console.log(findMedianSortedArrays([1,2],[-1,3]));